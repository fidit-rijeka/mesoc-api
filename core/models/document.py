import uuid

from django.contrib import auth
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FileField, FloatField, ForeignKey, ManyToManyField,
    Model, PROTECT, TextField, UUIDField, UniqueConstraint)

import magic
import fitz

from core.models.location import Location


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

    id = UUIDField(default=uuid.uuid4, primary_key=True)
    file = FileField(upload_to='documents/',)
    title = CharField(max_length=200, validators=(MinLengthValidator(1),), )
    abstract = TextField(max_length=1000, validators=(MinLengthValidator(1),))
    type = CharField(max_length=10, choices=TYPES.items())
    uploaded_at = DateTimeField(auto_now_add=True, blank=True)
    state = CharField(max_length=10, choices=STATES.items(), blank=True, default=PROCESSING)
    locations = ManyToManyField('core.Location', through='core.DocumentLocation', related_name='locations')
    language = ForeignKey('core.Language', on_delete=PROTECT)
    impacts = ManyToManyField('core.Impact', through='core.DocumentImpact', related_name='documents')
    user = ForeignKey(auth.get_user_model(), on_delete=CASCADE, related_name='documents')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._contents_cache = None

    @property
    def location(self):
        try:
            loc = self.locations.filter(documentlocation__primary=True).get()
        except Location.DoesNotExist:
            loc = None
            
        return loc

    @property
    def contents(self):
        if self.is_pdf:
            d = fitz.Document(stream=self._raw_contents, filetype='application/pdf')
            contents = '\n'.join(p.get_text() for p in d)
        else:
            contents = self._raw_contents.decode('utf-8')

        return contents

    @property
    def is_pdf(self):
        return magic.from_buffer(self._raw_contents, True) == 'application/pdf'

    @property
    def keywords_list(self):
        return self.keywords.values_list('value', flat=True)

    @property
    def _raw_contents(self):
        if not self._contents_cache:
            with self.file.open() as f:
                self._contents_cache = f.read()
        return self._contents_cache


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

    @property
    def keywords_list(self):
        return self.keywords.values_list('value', flat=True)


class DocumentLocation(Model):
    document = ForeignKey('core.Document', on_delete=CASCADE)
    location = ForeignKey('core.Location', on_delete=CASCADE)
    primary = BooleanField(default=True)
