def isPrimeNumber(num):
    # return true if th enumber is prime, false if not
    if num == 1 or num == 0:
        return False
    isPrime = True
    for divisor in range(2, num):
        calc = num % divisor        
        if calc == 0:
            isPrime = False
            return isPrime
    return isPrime


print(isPrimeNumber(9))

# print(f'numero: {num}')
# print(f'divisor: {divisor}')
# print(f'residuo: {calc}')

contPrimeNumbers = 0
numberToEvaluate = 1
sumPrimeNumber = 0

while contPrimeNumbers < 20:
    if isPrimeNumber(numberToEvaluate) == True:
        contPrimeNumbers = contPrimeNumbers + 1
        sumPrimeNumber = sumPrimeNumber + numberToEvaluate
        # print(numberToEvaluate)
        print(f'{numberToEvaluate}, {sumPrimeNumber}, {isPrimeNumber(sumPrimeNumber)}')
    numberToEvaluate = numberToEvaluate + 1
    

# identificar la primera secuencia de numeros primos cuya suma tambien es prima