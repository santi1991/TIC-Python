# fisrt in - first out
fila = [100, -500, 400, -100, 35, 20, 89]
print(fila)

# primera maner ad elograr una fila
# sacar valores de la ultima posicion y agregarlos en la posicion 0

# retirar un valor del final de la lisra
datoRetirado = fila.pop()
print(datoRetirado)
print(fila)

# inserta un valor al inicio de la lista
fila.insert(0, 7000)
print(fila)

def retirarProximoValor(lista):
    lista.pop()
    return lista

def insertarSiguiente(lista, elemento):
    lista.insert(0, elemento)
    return lista


# segunda manera de lograr una fila
# sacar valores de la primera y agregarlos al final de la lista
# retirar un valor del inicio de la lista

filaEjemplo2 = [40, -500, 800, 900, 1, -5, 8]
print(filaEjemplo2)

filaEjemplo2.pop(0)
print(filaEjemplo2)

# agregar un valor al final de la lista
filaEjemplo2.append(90)
print(filaEjemplo2)

def quitarSiguienteValor(lista):
    lista.pop(0)
    return lista


def agregarSiguienteValor(lista, elemento):
    lista.append(elemento)
    return lista