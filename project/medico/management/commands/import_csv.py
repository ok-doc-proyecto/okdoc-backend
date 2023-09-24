from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from medico.models import Especialidad

import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str, help='file path')
        parser.add_argument('--model', type=str, help='model to insert data')

    def handle(self, *args, **options):
        with open(options['csv_file'][0], 'r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            header = next(csvreader, None)

            model = apps.get_model('medico', options['model'])
            for row in csvreader:
                object_dict = {key: value for key, value in zip(header, row)}
                model.objects.create(**object_dict)
