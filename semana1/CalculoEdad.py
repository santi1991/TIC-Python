#Paso 1: Pedir la edad de la persona 1
edadPersona1 = input('Por favor, ingrese la edad de la primera persona: ')
#Paso 2: Pedir la edad de la persona 2
edadPersona2 = input('Por favor, ingrese la edad de la segunda persona: ')
# Paso 3: Calcular la diferencia de las edades
#nota: el ingreso de input es string, para hacer operaciones matematicas hay que cambiarla
diferencia = int(edadPersona1) - int(edadPersona2)
# Paso 4: Imprimir diferencia de las edades
print(f'La diferencia de las edades es {diferencia} años')