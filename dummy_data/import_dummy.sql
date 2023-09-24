.mode csv

--- Inserting especialidades
CREATE TEMP TABLE temp(especialidad);
.import especialidades.csv temp
INSERT INTO medico_especialidad(especialidad) SELECT * FROM temp;
DROP TABLE temp;

--- Inserting obras sociales
CREATE TEMP TABLE temp(obra_social);
.import obras_sociales.csv temp
INSERT INTO medico_obrasocial(obra_social) SELECT * FROM temp;
DROP TABLE temp;

--- Inserting medicos
CREATE TEMP TABLE temp(name, surname, date_added, rating);
.import medicos.csv temp
INSERT INTO medico_medico(name, surname, date_added, rating) SELECT * FROM temp;
DROP TABLE temp;

---Inserting reviews

CREATE TEMP TABLE temp(score, review, medico_id, date_added);
.import reviews.csv temp
INSERT INTO medico_review(score, review, medico_id, date_added) SELECT * FROM temp;
DROP TABLE temp;

--- Inserting relaciones medico-especialidad
CREATE TEMP TABLE temp(especialidad_id, medico_id);
.import rel_medico_especialidad.csv temp
INSERT INTO medico_relmedicoespecialidad(especialidad_id, medico_id) SELECT * FROM temp;
DROP TABLE temp;

--- Inserting relaciones medico-obra social
CREATE TEMP TABLE temp(medico_id, obra_social_id);
.import rel_medico_obra_social.csv temp
INSERT INTO medico_relmedicoobrasocial(medico_id, obra_social_id) SELECT * FROM temp;
DROP TABLE temp;