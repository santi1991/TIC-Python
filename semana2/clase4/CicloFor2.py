numberOfPersons = int(input('Por favor ingrese la cantidad de personas: '))

listOfAges = []
for i in range(0, numberOfPersons):
    listOfAges.append(int(input('Ingrese edad persona: ')))

print(listOfAges)

average = sum(listOfAges) / len(listOfAges)
print(f'el promedio de edad es: {average}')