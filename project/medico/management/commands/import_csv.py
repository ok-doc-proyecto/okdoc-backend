from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

import csv
import ast

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str, help='file path')
        parser.add_argument('--model', type=str, help='model to insert data')

    def handle(self, *args, **options):
        with open(options['csv_file'][0], 'r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            header = next(csvreader, None)

            model = apps.get_model('medico', options['model'])
            if options['model'] == 'medico':
                for row in csvreader:
                    obj = model.objects.create(first_name=row[0], last_name=row[1], date_added=row[2], rating=row[3])
                    especialidades = ast.literal_eval(row[4])
                    for especialidad_name in especialidades:
                        especialidad, _ = apps.get_model('medico', 'especialidad').objects.get_or_create(especialidad=especialidad_name)
                        obj.especialidades.add(especialidad)
                    
                    prepagas = ast.literal_eval(row[5])
                    for prepaga_name in prepagas:
                        prepaga, _ = apps.get_model('medico', 'prepaga').objects.get_or_create(prepaga=prepaga_name)
                        obj.prepagas.add(prepaga)

            elif options['model'] == 'usuario':
                for row in csvreader:
                    obj = model.objects.create(email=row[0], first_name=row[1], last_name=row[2], date_birth=row[3], date_added=row[4])

                    prepagas = ast.literal_eval(row[5])
                    for prepaga_name in prepagas:
                        prepaga, _ = apps.get_model('medico', 'prepaga').objects.get_or_create(prepaga=prepaga_name)
                        obj.prepagas.add(prepaga)

            elif options['model'] == 'review':
                for row in csvreader:
                    obj = model.objects.create(**{key: value for key, value in zip(header, row)})

            # for row in csvreader:
            #     object_dict = {}
            #     manytomany_fields = []

            #     for i, lst in enumerate(row):
            #         if type(lst) == list:
            #             model_fk = apps.get_model('medico', header[i])
            #             for value in lst:
            #                 p, created = model_fk.objects.get_or_create(value)

            #     for key, value in zip(header, row):
            #         if type(value) != list:
            #             object_dict[key] = value

            #         else:
            #             manytomany_fields.append((key, value))
            #     print(type(object_dict['prepaga']))
            #     obj = model.objects.create(**object_dict)
            #     for field in manytomany_fields:
            #         obj.field[0].add(*field[1:])
