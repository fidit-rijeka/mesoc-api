from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, FloatField, ForeignKey, IntegerField, Model, UniqueConstraint


class BaseCell(Model):
    class Meta:
        abstract = True
        constraints = (UniqueConstraint(fields=('document', 'cell'), name='%(app_label)s_%(class)s_unique_cell'),)

    classification = FloatField(validators=(MaxValueValidator(1.0), MinValueValidator(0.0)))
    cell = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))

    @property
    def cell_2d(self):
        return (self.cell // 3, self.cell % 3)


class Cell(BaseCell):
    document = ForeignKey('core.Document', CASCADE, 'cells')

    @property
    def user(self):
        return self.document.user  # required for object permission check


class HistoricalCell(BaseCell):
    document = ForeignKey('core.Document', CASCADE, 'historical_cells')

    @classmethod
    def from_cell(cls, cell_):
        return cls(classification=cell_.classification, cell=cell_.cell, document=cell_.document)
