numeroAEncontrar = 7
numeroIngresado = 0

while numeroIngresado != numeroAEncontrar: 
    numeroIngresado = int(input('Adivina cuál es el número: '))
    if numeroIngresado > numeroAEncontrar:
        print('El numero que estas buscando es menor al que ingresaste')
    elif numeroIngresado < numeroAEncontrar:
        print('El numero que estas buscando es mayor al que ingresaste')
    
print('Correcto! Adivinaste el numero')