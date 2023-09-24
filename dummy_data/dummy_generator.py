import os
import csv
import random
import string

from faker import Faker

dir_name = os.path.dirname(os.path.abspath(__file__))
fake = Faker('es_AR')

### Dummy data para especialidades ###
list_especialidades = ['Cardiología', 'Dermatología', 'Endocrinología', 'Gastroenterología', 'Geriatría', 'Ginecología', 
'Hematología', 'Nefrología', 'Neurología', 'Obstetricia', 'Odontología', 'Oftalmología', 'Oncología', 'Pediatría', 
'Psicología', 'Proctología', 'Psiquiatría', 'Reumatología', 'Urología']

sample_especialidades = [{'especialidad': i} for i in list_especialidades]

especialidades_csv = os.path.join(dir_name, 'especialidades.csv')

with open(especialidades_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=sample_especialidades[0].keys())
    writer.writeheader()
    writer.writerows(sample_especialidades)


### Dummy data para obras sociales ###
list_prepagas = ['Federada', 'Osde', 'Prevención Salud', 'Omint', 'Medicus', 'Avalian', 
'Plan de Salud Hospital Italiano', 'Sancor Salud', 'Galeno', 'William Hope']

sample_prepagas = [{'obra_social': i} for i in list_prepagas]

obras_csv = os.path.join(dir_name, 'obras_sociales.csv')

with open(obras_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=sample_prepagas[0].keys())
    writer.writeheader()
    writer.writerows(sample_prepagas)


### Dummy data para médicos ###
sample_medicos = []
for _ in range(50):
    medico = {'name': fake.first_name(), 'surname': fake.last_name(), 'date_added': fake.date(), 'rating': 0.00}
    sample_medicos.append(medico)

medicos_csv = os.path.join(dir_name, 'medicos.csv')

with open(medicos_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=sample_medicos[0].keys())
    writer.writeheader()
    writer.writerows(sample_medicos)


### Dummy data para reviews ###
reviews_csv = os.path.join(dir_name, 'reviews.csv')

with open(reviews_csv, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['score', 'review', 'medico_id', 'date_added'])

    for i in range(1001):
        score = random.randint(1, 5)
        review = ''.join(random.choice(string.ascii_letters+' ') for i in range(101))
        medico_id = random.randint(1, 50)
        date_added = fake.date()
        csvwriter.writerow([score, review, medico_id, date_added])


### Dummy data para relaciones medico-especialidad ###
relmedicoespecialidad_csv = os.path.join(dir_name, 'rel_medico_especialidad.csv')

with open(relmedicoespecialidad_csv, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['especialidad_id', 'medico_id'])
    
    # Se asegura de asignar al menos una especialidad por médico
    for medico in range(1, len(sample_medicos)+1):
        especialidad = random.randint(1, len(list_especialidades))
        csvwriter.writerow([especialidad, medico])
    
    # Asigna otras 30 especialidades a algunos médicos al azar
    for _ in range(30):
        especialidad = random.randint(1, len(list_especialidades))
        medico = random.randint(1, len(sample_medicos))
        csvwriter.writerow([especialidad, medico])


### Dummy data para relaciones medico-obra social ###
relmedicoobrasocial_csv = os.path.join(dir_name, 'rel_medico_obra_social.csv')

with open(relmedicoobrasocial_csv, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['obra_social_id', 'medico_id'])
    
    # Se asegura de asignar al menos una obra social por médico
    for medico in range(1, len(sample_medicos)+1):
        obra_social = random.randint(1, len(list_prepagas))
        csvwriter.writerow([obra_social, medico])
    
    # Asigna otras 30 obras sociales a algunos médicos al azar
    for _ in range(30):
        obra_social = random.randint(1, len(list_prepagas))
        medico = random.randint(1, len(sample_medicos))
        csvwriter.writerow([obra_social, medico])


### BORRA TODOS LOS DATOS en la database, mete los dummy data y borra los csv ###

os.system('python ../project/manage.py flush')

### La línea de abajo lo importa directamente desde sql, pero no pasa por la validación de django ###
# os.system('sqlite3 ../project/db.sqlite3 ".read import_dummy.sql"')
# os.remove(especialidades_csv)
# os.remove(obras_csv)
# os.remove(medicos_csv)
# os.remove(relmedicoespecialidad_csv)
# os.remove(relmedicoobrasocial_csv)
# os.remove(reviews_csv)