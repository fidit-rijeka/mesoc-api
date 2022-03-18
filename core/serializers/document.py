from django.conf import settings
from django.core.validators import FileExtensionValidator, MinLengthValidator

from rest_framework.reverse import reverse
from rest_framework.serializers import (
    CharField, FileField, HyperlinkedModelSerializer, SerializerMethodField, ValidationError
)

from core.models import Document, Location
from core.serializers.language import LanguageSerializer
from core.serializers.location import LocationSerializer
from core.validators import FileMaxSizeValidator, FileMimeTypeValidator


class BaseDocumentSerializer(HyperlinkedModelSerializer):
    def get_heatmap(self, obj):
        return reverse('document-heatmap', args=(obj.pk,), request=self.context['request'])

    def get_impacts(self, obj):
        return reverse('document-impacts', args=(obj.pk,), request=self.context['request'])

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
            'heatmap',
            'impacts',
            'user',
            'url',
        )
        read_only_fields = ('uploaded_at', 'language', 'url')


class DocumentUploadSerializer(BaseDocumentSerializer):
    title = CharField(max_length=100, validators=(MinLengthValidator(1),))
    location = CharField(max_length=142, required=False)
    heatmap = SerializerMethodField(read_only=True)
    impacts = SerializerMethodField(read_only=True)
    user = SerializerMethodField(read_only=True)
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
            'heatmap',
            'impacts',
            'user',
            'file',
            'url',
        )
        read_only_fields = ('uploaded_at', 'state', 'url')

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
