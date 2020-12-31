from django.db.models import CharField, Model


class Country(Model):
    name = CharField(max_length=56)
