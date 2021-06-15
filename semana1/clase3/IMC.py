# paso 1: pedir peso
peso = int(input('Ingrese peso en kg: '))

# paso 2: pedir statura
estatura = float(input('Ingrese estatura en m: '))

# calcular imc
imc = peso/(estatura**2)

# mostarar imc
# print(f'su imc es {imc} kg/m2')

# cualquier cosa que siga a la derecha del if es la ejecucion
# mostrar imc dependiento del caso
if imc >= 25:
    print(f'Ojo, tienes sobrepeso. Tu IMC es {imc} kg/m2')
else:
    print(f'No tienes sobrepeso. Tu IMC es {imc} kg/m2')