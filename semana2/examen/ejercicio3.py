# Elabore un programa en Python que lea dos datos enteros correspondiente a los lados de un rectángulo 
# e imprima el área y el perímetro.
base = int(input('ingresa el valor de la base del rectangulo: '))
altura = int(input('ingresal el valor de la altura del rectangulo: '))
area = base * altura
perimetro = 2 * ( base + altura )
area = print(f'el area del rectangulo es: {area} y su perimetro es {perimetro}')