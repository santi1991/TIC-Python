listNumbers = [-10, 50, 800, 9, 6, 23.5]

count = 0

print(len(listNumbers))

for element in listNumbers:
    count += 1

print(f'total elementos en la lista es {count}')

suma = 0
for element in listNumbers:
    suma = suma + element

print(f'total suma en la lista es {suma}')
print(f'promedio de la lista es {suma/count}')