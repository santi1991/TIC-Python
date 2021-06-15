# Elabore un programa en Python que lea una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit y muestre el resultado con un mensaje bien explicativo.
# No use aproximaciones

# ingresar valor en gradospedir Celsius
valorCelsius = int(input('Ingrese la temperatura en grados Celsius: '))
# formula para aplicar conversion entre C a F
valorFahrenheit = (valorCelsius * 9/5) + 32
# mostrar resultado
print(f'el valor en valorFahrenheit es {valorFahrenheit}')
# FahToCel = (valorFahrenheit - 32) / (9/5)
# print(f'el valor en celciuos es {FahToCel}')