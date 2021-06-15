from vector import vector
import random
import math

# """Esta funcion invierte un número, osea, 3456 invertido sería 6543"""
def invierteNumero(n): 
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10 # returns the last digit of the number
        nunu = nunu * 10 + digito
        m = m // 10
    return nunu

# """Esta función retorna el primer digito de el número x"""
def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

# """Funcion que contiene la solución al problema que será calificado"""
def solucion():
    # """Se genera aleatoriamente un número entero entre 15 y 30"""
    #  ***** --> n = #numero random entre 15 y 30, Use random.randint()
    # n = random.randint(15, 30)
    n = 5
    # """A 's' se le asigna un 0, esta variable va ser donde se almacena la suma como esta descrito en el enunciado"""
    s = 0 
    # """Se crea un objeto vector que tiene como tamaño el valor n"""
    vec4 = vector(n)
    # vec4 = [154, 6412, 74595, 77877, 4862, 96325]
    # vec4 = [0] * (5 + 1)
    # """Usamos un ciclo para llenar el vector con número del 1 al 99999"""
    for i in range(1, n + 1):
        # """Se genera aleatoriamente un número entero entre 1 y 99999"""
        # ----->  vec4.V[i] = #numero random entre 1 y 99999, Use random.randint()
        # vec4.V[i] = random.randint(1, 99999)        
        # """Se actualiza el valor de la primera posición del vector indicando cuantas posiciones
        # son usadas (En este caso es igual al tamaño del vector)"""
        # vec4.V[0] = n
        vec4.V = [154, 6412, 74595, 77877, 4862, 96325]
        # vec4.V[0] = n
    # """Usamos un ciclo para recorrer el vector"""
    for i in range(0, len(vec4.V)):
        print(f'**elementos vector {vec4.V[i]}')
        # """En la variable 'nunu' sea almacena el numero invertido de la posición i del vector"""
        nunu = invierteNumero(vec4.V[i])
        # """Se pregunta si al invertir el numero sige siendo el mismo(capicua) o si el numero compienza por un dígito par"""
        if vec4.V[i] == nunu or comienzaCon(vec4.V[i]) % 2 == 0:
            print(f'elementos a sumar {vec4.V[i]}')
            # """Se realiza la suma de la suma acumulada
            # con el dato en la posición i"""
            #  ---->  s += #Acumule la suma
            # s = s + vec4.V[i]  ---> ASI LO USO YO
            s += vec4.V[i]
            print(f'suma {s}')
    # """Se retornan los objetos requeridos para efectuar la
    # calificación de la solución"""
    return vec4, s

# numero = int(input('ingresa un numero: '))
# print(f'numero {numero} y reves: {invierteNumero(numero)}')
solVector = solucion()

# print(f'{solVector}')