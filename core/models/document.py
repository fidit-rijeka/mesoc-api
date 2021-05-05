import uuid

from django.contrib import auth
from django.core.validators import MinLengthValidator
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FileField, ForeignKey, IntegerField, ManyToManyField, Model,
    PROTECT, UUIDField
)


class Document(Model):
    PROCESSING = 0
    FAILED = 1
    PROCESSED = 2
    DISMISSED = 3

    STATES = {
        PROCESSING: 'processing',
        FAILED: 'failed',
        PROCESSED: 'processed',
        DISMISSED: 'dismissed'  # failure acknowledged by the user
    }

    class Meta:
        unique_together = ('file_title', 'user')

    id = UUIDField(default=uuid.uuid4, primary_key=True)
    file = FileField(upload_to='documents/',)
    file_title = CharField(max_length=200, validators=(MinLengthValidator(1),),)
    document_title = CharField(blank=True, default='', max_length=200, validators=(MinLengthValidator(1),))
    uploaded_at = DateTimeField(auto_now_add=True, blank=True)
    state = IntegerField(choices=STATES.items(), blank=True, default=PROCESSING)
    cities = ManyToManyField('core.City', through='core.DocumentCity', related_name='cities')
    language = ForeignKey('core.Language', on_delete=PROTECT)
    user = ForeignKey(auth.get_user_model(), on_delete=CASCADE, related_name='documents')

    @property
    def location(self):
        return self.cities.filter(documentcity__primary=True).get()


class DocumentCity(Model):
    document = ForeignKey('core.Document', on_delete=CASCADE)
    city = ForeignKey('core.City', on_delete=CASCADE)
    primary = BooleanField(default=True)


class DocumentKeyword(Model):
    document = ForeignKey('core.Document', on_delete=CASCADE, related_name='keywords')
    value = CharField(max_length=100)
