from django.conf import settings
from django.core.validators import FileExtensionValidator, MinLengthValidator

from rest_framework.reverse import reverse
from rest_framework.serializers import (
    CharField, FileField, HyperlinkedModelSerializer, IntegerField, ListField, Serializer, SerializerMethodField,
    ValidationError
)

from core.models import Document, Location, Cell, HistoricalCell
from core.serializers.language import LanguageSerializer
from core.serializers.location import LocationSerializer
from core.validators import FileMaxSizeValidator, FileMimeTypeValidator


class BaseDocumentSerializer(HyperlinkedModelSerializer):
    def get_heatmap(self, obj):
        return reverse('document-heatmap', args=(obj.pk,), request=self.context['request'])

    def get_impacts(self, obj):
        return reverse('document-impacts', args=(obj.pk,), request=self.context['request'])

    def get_classification(self, obj):
        return reverse('document-classification', args=(obj.pk,), request=self.context['request'])

    def get_user(self, obj):
        return reverse('account', request=self.context['request'])

    def get_language(self, obj):
        return LanguageSerializer(obj.language, context=self.context).data

    def get_location(self, obj):
        return LocationSerializer(obj.location, context=self.context).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['language'] = self.get_language(instance)
        representation['location'] = self.get_location(instance)
        return representation


class DocumentSerializer(BaseDocumentSerializer):
    title = CharField(max_length=100, validators=(MinLengthValidator(1),), read_only=True)
    heatmap = SerializerMethodField()
    impacts = SerializerMethodField()
    classification = SerializerMethodField()
    user = SerializerMethodField()

    class Meta:
        model = Document
        fields = (
            'title',
            'abstract',
            'type',
            'uploaded_at',
            'state',
            'language',
            'location',
            'reclassified',
            'heatmap',
            'impacts',
            'classification',
            'user',
            'url',
        )
        read_only_fields = ('uploaded_at', 'language', 'reclassified')


class DocumentUploadSerializer(BaseDocumentSerializer):
    title = CharField(max_length=100, validators=(MinLengthValidator(1),))
    location = CharField(max_length=142, required=False)
    heatmap = SerializerMethodField()
    impacts = SerializerMethodField()
    classification = SerializerMethodField()
    user = SerializerMethodField()
    file = FileField(
        allow_empty_file=False,
        write_only=True,
        validators=(
            FileMaxSizeValidator(settings.CORE_FILE_MAX_SIZE),
            FileExtensionValidator(settings.CORE_ALLOWED_EXTENSIONS),
            FileMimeTypeValidator(settings.CORE_ALLOWED_MIME_TYPES)
        )
    )

    class Meta:
        model = Document
        fields = (
            'title',
            'abstract',
            'type',
            'uploaded_at',
            'state',
            'language',
            'location',
            'reclassified',
            'heatmap',
            'impacts',
            'classification',
            'user',
            'file',
            'url',
        )
        read_only_fields = ('uploaded_at', 'state', 'reclassified')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        location = validated_data.pop('location', None)
        if location is None:
            location = Location.objects.filter(city='Unknown', country='Unknown').get()
        else:
            if location.pk is None:
                location.save()

        obj = super().create(validated_data)
        DocumentLocation = self.Meta.model.locations.through
        DocumentLocation(document=obj, location=location, primary=True).save()

        return obj

    def validate_title(self, value):
        Document = self.Meta.model
        qs = Document.objects.filter(title=value, state=Document.PROCESSED, user=self.context['request'].user)
        if qs.exists():
            raise ValidationError('Document with the same title already exists.', code='invalid')

        return value

    def validate_location(self, value):
        loc = Location.search_api(address=value)
        if len(loc) == 0:
            raise ValidationError('Location with the specified address not found.', code='invalid')
        if len(loc) != 1:
            raise ValidationError('Location with the specified address is not unique.', code='invalid')
        else:
            loc = loc[0]

        return loc


class DocumentClassificationSerializer(Serializer):
    cells = ListField(child=IntegerField(min_value=0, max_value=29), max_length=30, allow_empty=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if self.instance.reclassified:
            raise ValidationError('Document has already been reclassified.')

        return validated_data

    def save(self, **kwargs):
        cells = {cell.cell: cell for cell in self.instance.cells.all()}

        existing_cells = set(cells.keys())
        classified_cells = set(self.validated_data['cells'])
        delete_cells = existing_cells - classified_cells

        update_cells = []
        create_cells = []
        historical_cells = []

        for cell in classified_cells:
            if cell in existing_cells:
                existing_cell = cells[cell]

                historical_cells.append(HistoricalCell.from_cell(existing_cell))

                existing_cell.classification = 1.0
                update_cells.append(existing_cell)
            else:
                create_cells.append(Cell(cell=cell, classification=1.0, document=self.instance))

        for cell in delete_cells:
            historical_cells.append(HistoricalCell.from_cell(cells[cell]))

        Cell.objects.bulk_create(create_cells)
        Cell.objects.bulk_update(update_cells, ('classification',))

        HistoricalCell.objects.bulk_create(historical_cells)

        self.instance.cells.filter(cell__in=delete_cells).delete()

        self.instance.reclassified = True
        self.instance.save()
