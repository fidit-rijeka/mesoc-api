from django.conf import settings

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..models import RepositoryDocument


class SimilarDocumentSerializer(ModelSerializer):
    preview_url = SerializerMethodField()
    similarity = SerializerMethodField()

    class Meta:
        model = RepositoryDocument
        fields = ('document_title', 'similarity', 'preview_url')

    def get_preview_url(self, obj):
        return '{}/{}.html'.format(settings.CORE_REPOSITORY_PREVIEW_URL, obj.id)

    def get_similarity(self, obj):
        return self.context['similarities'][obj.pk]
