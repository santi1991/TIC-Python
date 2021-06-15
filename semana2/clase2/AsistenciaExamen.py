# ejercicio 5: mostrar si un estudiante esta habilitado para presentar un examen
# si el estudiante fue a mas del 75% de las clases puede hacer el examen
# menos del 75%, solo puede hacerlo si tiene excusa medica
totalClases = int(input('ingrese total clases: '))
clasesAsistidas = int(input('ingrese a cuantas de esas clases asistio el estudiante: '))
porcentajeAsistencia = clasesAsistidas / totalClases
if porcentajeAsistencia > 0.75:
    print('puede asistir al examen')
else:
    tieneExcusa = input('Estudiante tiene excusa medica?: ').lower()
    if tieneExcusa == 'si' or tieneExcusa == 'sí':
        print('puede presentar examen')
    else:
        print('no puede presentar examen')