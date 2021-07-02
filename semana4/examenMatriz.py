import numpy as np


matrizEjemplo = np.array([[89, 13, 23, 72],
                        [29, 11, 81, 62],
                        [27, 26, 88, 33],
                        [ 5, 78, 11, 11]])

def solucion(A):
    n = A.shape[0]
    print(f'dimension {n}')
    sum_diagonal_principal = 0
    prod_diagonal_secundaria = 1
    # resultado2_mod_resultado1 = prod_diagonal_secundaria % sum_diagonal_principal

    for index, data in np.ndenumerate(A):
        # identificar el valor de i y j de cada dato de la matriz
        i = index[0]
        j = index[1]        
        # identificar si un dato está en la diagonal principal
        if i == j:
            # print("diagonal ppal: ", data)        
            sum_diagonal_principal = sum_diagonal_principal + data
        # if (n - i - 1) == j:
        if (i + j) == (n-1):
            print("diagonal inversa", data)
            prod_diagonal_secundaria = prod_diagonal_secundaria * data


    print(f'suma diagonal ppal: {sum_diagonal_principal}')
    print(f'producto diagonal secundaria: {prod_diagonal_secundaria}')
    resultado2_mod_resultado1 = prod_diagonal_secundaria % sum_diagonal_principal
    print(f'modulo: {resultado2_mod_resultado1}')

    

    
    
    # return sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1

solucion(matrizEjemplo)

    