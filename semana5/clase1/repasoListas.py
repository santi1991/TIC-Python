# definir una lista
lista = [1, 5, 7, 9, -12, 1, 230]
        #0, 1, 2, 3,  4,  5
# imprimir una lista
# print(lista)

# accede a un dato a traves del indice
lista[2] = -50

# print(lista)

# imprimir un dato en especifico
# print(lista[4])

# agregar un dato a la lista
lista.append(-69)
# print(lista)

# agregar un dato en una posicion especifica  (posicion, dato)
lista.insert(1, 4)
# print(lista)

# eliminar dato de una lista a traves de su valor (hasta que lo encuentra de derecha a izquierda)
lista.remove(-50)
print(lista)

# elimina el primer dato
lista.remove(lista[0])
print(lista)

# eliminar ultimo valor de la lista
lista.pop()
print(lista)

# eliminar valor segun posicion
lista.pop(2)
print(lista)

# organziar una lista
lista.sort()
print(lista)

# revisar si un valor pertenece a la lista
print(-500 in lista)
print(5 in lista)

# reviar logitud de la lista
print(len(lista))

# slicing desde una posicion de inicio hasta un final
print(lista[1:3])
# desde la posicion cero hasta un indice especificado
print(lista[:3])
# a partir de un indice hasta el final
print(lista[2:])