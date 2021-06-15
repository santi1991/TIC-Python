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
# 18.5 < imc < 24.9
if imc < 18.5:
    print(f'Tienes una condicion de peso inferior al normal.')
elif imc >= 18.5 and imc < 25: 
    print(f'Tiene una condicion de peso normal.')
elif imc >= 25 and imc < 30:
    print(f'Tiene un peso superior al normal.')
else:
    print(f'Usted tiene sobrepeso. ')
print(f'Tu IMC es {imc} kg/m2')