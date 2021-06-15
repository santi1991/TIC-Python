import random

# n = int(input('Entre tamaño del vector: '))

V = [0] * (5 + 1)

def construyeVector(n):
    # V[0] = n
    for i in range(0, n + 1):
        V[i] = random.randint(1, 99)
    return V

print(construyeVector(5))