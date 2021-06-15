import random

def machineSelection():
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        return 'R'
    elif randomNumber == 2:
        return 'P'
    elif randomNumber == 3:
        return 'S'

# machine = machineSelection()
# print(machine)

# user = input('Ingresa tu seleccion (R, P, S): ')


contP1 = 0
contP2 = 0

while contP1 < 2 and contP2 < 2:
    player1 = input('ingrese R, P o S: ')
    machine = machineSelection()
    # machine = input('ingrese R, P o S: ')

    if player1 == machine:
        print('empate')

    if player1 == 'R' and machine == 'S':
        print('juador 1 gana')
        contP1 = contP1 + 1
    elif machine == 'R' and player1 == 'S':
        print('machine gana')
        contP2 = contP2 + 1

    if player1 == 'P' and machine == 'R':
        print('jugador 1 gana')
        contP1 = contP1 + 1
    elif machine == 'P' and player1 == 'R':
        print('machine gana')
        contP2 = contP2 + 1
        
    if player1 == 'S' and machine == 'P':
        contP1 = contP1 + 1
        print('machine gana')
    elif machine == 'S' and player1 == 'P':
        contP2 = contP2 + 1
        print('jugador 2 gana')

    print(f'el jugador 1 ha ganado: {contP1}')
    print(f'machine ha ganado: {contP2}')
if contP2 == 2:
    print('machine ganó')
elif contP1 == 2:
    print('el jugador 1 ganó')
