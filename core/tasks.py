import json
import random

from django.core import mail
from celery import shared_task

from .models import Cell, CellVariable, Document, Variable


@shared_task
def send_mail(subject, message, from_, to):
    mail.send_mail(subject, message, from_, to)


@shared_task
def process_document(document):
    id_ = document['url'].split('/')[-2]
    instance = Document.objects.filter(id=id_).get()
    test_results = [
        'core/example_results/0_document.json',
        'core/example_results/1_document.json',
        'core/example_results/2_document.json',
        'core/example_results/3_document.json',
        'core/example_results/4_document.json'
    ]
    result = random.choice(test_results)

    existing_variables = dict((v.pk, v) for v in Variable.objects.all())

    # TODO: actually process the document
    with open(result) as f:
        result = json.load(f)

        instance.document_title = result['title']

        for c in result['cells']:
            variables = c.pop('variables')
            cell = Cell(document=instance, **c)
            cell.save()
            for v in variables:
                id_, name = v.pop('id'), v.pop('name')
                if id_ in existing_variables:
                    variable = existing_variables[id_]
                else:
                    variable = Variable.objects.create(id=id_, name=name)
                    variable.save()
                    existing_variables[id_] = variable

                CellVariable(cell=cell, variable=variable, **v).save()

    instance.state = instance.PROCESSED
    instance.save()
