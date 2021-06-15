

contP1 = 0
contP2 = 0

while contP1 < 2 and contP2 < 2:
    player1 = input('ingrese R, P o S: ')
    player2 = input('ingrese R, P o S: ')

    if player1 == player2:
        print('empate')

    if player1 == 'R' and player2 == 'S':
        print('juador 1 gana')
        contP1 = contP1 + 1
    elif player2 == 'R' and player1 == 'S':
        print('jugador 2 gana')
        contP2 = contP2 + 1

    if player1 == 'P' and player2 == 'R':
        print('jugador 1 gana')
        contP1 = contP1 + 1
    elif player2 == 'P' and player1 == 'R':
        print('jugador 2 gana')
        contP2 = contP2 + 1
        
    if player1 == 'S' and player2 == 'P':
        contP1 = contP1 + 1
        print('jugador 1 gana')
    elif player2 == 'S' and player1 == 'P':
        contP2 = contP2 + 1
        print('jugador 2 gana')

    print(f'el jugador 1 ha ganado: {contP1}')
    print(f'el jugador 2 ha ganado: {contP2}')
if contP2 == 2:
    print('el jugador 2 ganó')
elif contP1 == 2:
    print('el jugador 1 ganó')
