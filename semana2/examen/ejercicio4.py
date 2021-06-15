# Elabore programa en Python que le permita al usuario ingresar números enteros de manera indefinida, 
# hasta que ingrese un número negativo, 
# y al final imprimir la suma de los números enteros pares sin incluir el número negativo en la suma.
a = 1 % 2
print(a)

# numero = int(input('Ingresa un numero entero: '))
numero = 0
listOfNumbers = []
while numero >= 0:
    numero = int(input('Ingresa un numero entero: '))
    esNumeroPar = numero % 2
    if esNumeroPar == 0 and numero > 0:
        listOfNumbers.append(numero)
print(f'Ingresaste un numero negativo! la suma total fue: {sum(listOfNumbers)}!')