
# Elabore un programa en Python que lea un entero de dos dígitos y produzca como salida
# los dígitos del número leído con su correspondiente mensaje. Por ejemplo, si el número leído es 27, 
# la salida deberá ser:(sin texto adicional):
# 2
# 7

numero = int(input('Ingrese un número de dos dígitos: '))

while numero < 10 or numero >= 100:
    numero = int(input('Ojo! ingresa el numero que sea de dos digitos: '))
texto = str(numero)
for i in range(0, len(texto)):
    print(texto[i])