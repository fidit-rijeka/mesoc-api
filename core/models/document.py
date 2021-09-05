import uuid

from django.contrib import auth
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FileField, FloatField, ForeignKey, IntegerField, ManyToManyField,
    Model, PROTECT, TextField, UUIDField, UniqueConstraint)

import magic
import fitz


class Document(Model):
    PROCESSING = 'processing'
    FAILED = 'failed'
    PROCESSED = 'processed'
    DISMISSED = 'dismissed'

    SCIENTIFIC = 'scientific'
    PILOT = 'pilot'

    STATES = {
        PROCESSING: 'processing',
        FAILED: 'failed',
        PROCESSED: 'processed',
        DISMISSED: 'dismissed'  # failure acknowledged by the user
    }

    TYPES = {
        SCIENTIFIC: SCIENTIFIC,
        PILOT: PILOT
    }

    class Meta:
        unique_together = ('file_title', 'user')

    id = UUIDField(default=uuid.uuid4, primary_key=True)
    file = FileField(upload_to='documents/',)
    file_title = CharField(max_length=200, validators=(MinLengthValidator(1),),)
    document_title = CharField(blank=True, default='', max_length=200, validators=(MinLengthValidator(1),))
    abstract = TextField(max_length=1000, validators=(MinLengthValidator(1),))
    type = CharField(max_length=10, choices=TYPES.items())
    uploaded_at = DateTimeField(auto_now_add=True, blank=True)
    state = CharField(max_length=10, choices=STATES.items(), blank=True, default=PROCESSING)
    cities = ManyToManyField('core.City', through='core.DocumentCity', related_name='cities')
    language = ForeignKey('core.Language', on_delete=PROTECT)
    impacts = ManyToManyField('core.Impact', through='core.DocumentImpact', related_name='documents')
    user = ForeignKey(auth.get_user_model(), on_delete=CASCADE, related_name='documents')

    @property
    def location(self):
        return self.cities.filter(documentcity__primary=True).get()

    @property
    def contents(self):
        with self.file.open() as f:
            contents = f.read()
            if magic.from_buffer(contents, True) == 'application/pdf':
                d = fitz.Document(stream=contents, filetype='application/pdf')
                contents = '\n'.join(p.get_text() for p in d)
            else:
                contents = contents.decode('utf-8')

        return contents


class DocumentCity(Model):
    document = ForeignKey('core.Document', on_delete=CASCADE)
    city = ForeignKey('core.City', on_delete=CASCADE)
    primary = BooleanField(default=True)


class DocumentKeyword(Model):
    document = ForeignKey('core.Document', on_delete=CASCADE, related_name='keywords')
    value = CharField(max_length=100)


class DocumentImpact(Model):
    class Meta:
        constraints = (
            UniqueConstraint(fields=('document', 'impact'), name='unique_document_impact'),
        )

    strength = FloatField(validators=(MinValueValidator(0.0), MaxValueValidator(1.0)))
    document = ForeignKey('core.Document', CASCADE, related_name='document_impacts')
    impact = ForeignKey('core.Impact', CASCADE, related_name='impact_documents')
    keywords = ManyToManyField('core.ImpactKeyword', related_name='document_impacts')
