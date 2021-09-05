from django.conf import settings
from django.core.validators import FileExtensionValidator, MinLengthValidator

from rest_framework.reverse import reverse
from rest_framework.serializers import (
    CharField, FileField, HyperlinkedModelSerializer, HyperlinkedRelatedField, SerializerMethodField, ValidationError
)

from ..models import City, Document
from ..serializers.city import CitySerializer
from ..serializers.language import LanguageSerializer
from ..validators import FileMaxSizeValidator, FileMimeTypeValidator


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
        return CitySerializer(obj.location, context=self.context).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['language'] = self.get_language(instance)
        representation['location'] = self.get_location(instance)
        return representation


class DocumentSerializer(BaseDocumentSerializer):
    title = CharField(max_length=100, validators=(MinLengthValidator(1),), source='file_title', read_only=True)
    location = HyperlinkedRelatedField(view_name='city-detail', read_only=True)
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
    title = CharField(max_length=100, validators=(MinLengthValidator(1),), source='file_title',)
    location = HyperlinkedRelatedField(view_name='city-detail', queryset=City.objects.exclude(name='Unknown'))
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
        city = validated_data.pop('location')
        validated_data['user'] = self.context['request'].user
        obj = super().create(validated_data)
        obj.cities.add(city)

        return obj

    def validate_title(self, value):
        if self.Meta.model.objects.filter(file_title=value, user=self.context['request'].user).exists():
            raise ValidationError('Document with the same title already exists.', code='invalid')

        return value
