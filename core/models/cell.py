from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, FloatField, ForeignKey, IntegerField, ManyToManyField, Model


class Cell(Model):
    class Meta:
        unique_together = ('document', 'order')

    classification = FloatField(validators=(MaxValueValidator(1.0), MinValueValidator(0.0)))
    order = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    document = ForeignKey('core.Document', CASCADE, 'cells')
    variables = ManyToManyField('core.Variable',  through='core.CellVariable',)

    @property
    def user(self):
        return self.document.user  # required for object permission check


class CellVariable(Model):
    class Meta:
        unique_together = ('cell', 'variable')

    cell = ForeignKey('core.Cell', CASCADE)
    variable = ForeignKey('core.Variable', CASCADE)
    num_ontology_categories = IntegerField(validators=(MinValueValidator(1),))
    num_keyword_vars = IntegerField(validators=(MinValueValidator(1),))
    strength = FloatField(validators=(MaxValueValidator(1.0), MinValueValidator(0.0)))
