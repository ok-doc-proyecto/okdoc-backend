import os
import csv
import random
import string
from datetime import date

from faker import Faker

dir_name = os.path.dirname(os.path.abspath(__file__))
fake = Faker('es_AR')


### Dummy data para médicos ###
list_especialidades = ['Cardiología', 'Dermatología', 'Endocrinología', 'Gastroenterología', 'Geriatría', 'Ginecología', 
'Hematología', 'Nefrología', 'Neurología', 'Obstetricia', 'Odontología', 'Oftalmología', 'Oncología', 'Pediatría', 
'Psicología', 'Proctología', 'Psiquiatría', 'Reumatología', 'Urología']

list_prepagas = ['Federada', 'Osde', 'Prevención Salud', 'Omint', 'Medicus', 'Avalian', 
'Plan de Salud Hospital Italiano', 'Sancor Salud', 'Galeno', 'William Hope']

medicos_csv = os.path.join(dir_name, 'medicos.csv')

with open(medicos_csv, 'w', newline='', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['first_name', 'last_name', 'date_added', 'rating', 'especialidades', 'prepagas'])
    
    for _ in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_added = fake.date()
        rating = 0.00
        especialidades = random.sample(list_especialidades, k=random.randint(1,3))
        prepagas = random.sample(list_prepagas, k=random.randint(1,4))
        csvwriter.writerow([first_name, last_name, date_added, rating, especialidades, prepagas])


### Dummy data para reviews ###
reviews_csv = os.path.join(dir_name, 'reviews.csv')

with open(reviews_csv, 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['score', 'review', 'medico_id', 'date_added', 'usuario_id'])

    for i in range(1000):
        score = random.randint(1, 5)
        review = ''.join(random.choice(string.ascii_letters+' ') for i in range(100))
        medico_id = random.randint(1, 50)
        date_added = fake.date()
        usuario_id = random.randint(1, 250)
        csvwriter.writerow([score, review, medico_id, date_added, usuario_id])


### Dummy data para usuarios ###
usuarios_csv = os.path.join(dir_name, 'usuarios.csv')

with open(usuarios_csv, 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['email', 'first_name', 'last_name', 'date_birth', 'date_added', 'prepagas'])

    for _ in range(250):
        email = fake.ascii_email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_birth = fake.date_between_dates(date_start=date(1950,1,1), date_end=date.today())
        date_added = fake.date_between_dates(date_start = date_birth, date_end=date.today())
        prepagas = random.sample(list_prepagas, k=random.randint(1,3))
        csvwriter.writerow([email, first_name, last_name, date_birth, date_added, prepagas])