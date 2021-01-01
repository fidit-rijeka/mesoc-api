from django.core.exceptions import ValidationError

import magic


class FileMaxSizeValidator:
    def __init__(self, max_bytes):
        self._max_bytes = max_bytes

    def __call__(self, value):
        if value.size > self._max_bytes:
            raise ValidationError('File exceeds {} bytes.'.format(self._max_bytes), code='invalid')


class FileMimeTypeValidator:
    def __init__(self, allowed_mime_types):
        self._allowed_mime_types = allowed_mime_types

    def __call__(self, value):
        mime = magic.from_buffer(value.file.read(2048), True)
        if mime not in self._allowed_mime_types:
            raise ValidationError(
                'File type is not valid, allowed: {}.'.format(','.join(self._allowed_mime_types)),
                code='invalid'
            )
