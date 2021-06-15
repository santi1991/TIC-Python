import random

def guessTheNumber(maxRetries):
    numberToGuess = random.randint(0, 20)
    print(numberToGuess)

    # numero max de intentos
    maxGuess = maxRetries

    countUserGuess = 0

    won = False

    while countUserGuess < maxGuess and not won:
        userInput = int(input('Adivina el numero entre 0 y 20: '))
        if userInput == numberToGuess:
            print('Ganaste!')
            won = True
        else:
            print('No adivinaste...')
            countUserGuess = countUserGuess + 1
            print(f'Te quedan {maxGuess - countUserGuess} intentos')

    if (countUserGuess == maxGuess):
        print(f'Has perdido!, el numero a adivinar era: {numberToGuess}')

guessTheNumber(3)