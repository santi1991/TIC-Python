calificacion = float(input('ingrese calificacion: '))
if calificacion >= 0 and calificacion <= 5:
    if calificacion >= 0 and calificacion < 3: 
        print('calificacion insuficiente')
    elif calificacion >= 3 and calificacion < 4:
        print('calificacion aceptable')
    elif calificacion >= 4 and calificacion < 4.6:
        print('calificacion sobresaliente')
    else:
        print('calificacion excelente')
else:
    print('calificacion invalida')