from django.db.models import CharField, IntegerField, ManyToManyField, Model


class Impact(Model):
    value = CharField(max_length=100)
    lemma = CharField(max_length=100)
    column = IntegerField(choices=((i, i) for i in range(3)))
    keywords = ManyToManyField('core.ImpactKeyword', related_name='impacts')

    def __str__(self):
        return self.value


class ImpactKeyword(Model):
    value = CharField(max_length=100)

    def __str__(self):
        return self.value
