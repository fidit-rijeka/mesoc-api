from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, FloatField, ForeignKey, IntegerField, Model


class Cell(Model):
    class Meta:
        unique_together = ('document', 'order')

    classification = FloatField(validators=(MaxValueValidator(1.0), MinValueValidator(0.0)))
    order = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    document = ForeignKey('core.Document', CASCADE, 'cells')

    @property
    def user(self):
        return self.document.user  # required for object permission check
