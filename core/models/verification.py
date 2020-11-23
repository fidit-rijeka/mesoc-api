import uuid

from django.contrib import auth
from django.db import models


class Verification(models.Model):
    id = models.UUIDField(primary_key=True, blank=True, default=uuid.uuid4)
    user = models.OneToOneField(auth.get_user_model(), models.CASCADE)
