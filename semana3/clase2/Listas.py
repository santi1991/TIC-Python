myList = [1, 34, 52, 87, -25, 90]

# imprimir un elemento en especifico 
print(myList[2])

# se puede modificar un elemento especifico a traves de su indice
myList[4] = -69
print(myList)

# los indices negativo devuelven la posicion de derecha a izquierda
print(myList[-2])

# agregar un elemento al final de la lista
myList.append(120)
print(myList)

# eliminar valor de una lista
myList.remove(34)
print(myList)

# agregar valor en la posicion que quiera (posicion, valor)
myList.insert(0, 500)
print(myList)

# eliminar dato por su indice
del myList[4]
print(myList)

# obtener y eliminar el último elemento de la lista
elementoEliminado = myList.pop()
print(elementoEliminado)
print(myList)

# conocer cuando elementos tiene una lista
print(f'la lista tiene {len(myList)} elements')

# sumar los elementos
print(f'la suma lista es {sum(myList)}')

# identificar si un elemento hace parte de una lista
print(1 in myList)
print(-3445 in myList)

# ordenar de manera ascendente
myList.sort()
print(myList)

# ordenar de manera descendente
myList.reverse()
print(myList)

# calcular el max de una lista
print(max(myList))

# calcular el min de una lista
print(min(myList))


