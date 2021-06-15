

def addTwoNumbers(n1, n2):
    sum = n1 + n2
    return sum

def restNumbers(n1, n2):
    return n1 - n2

def multiplyNumbers(n1, n2):
    return n1 * n2

def calculateResult(n1, n2, operation):
    if operation == 's':
        return addTwoNumbers(num1, num2)
    elif operation == 'r':
        return restNumbers(num1, num2)
    elif operation == 'm':
        return multiplyNumbers(num1, num2)
    else:
        return 'error'

num1 = int(input('ingrese numero1: '))
num2 = int(input('ingrese numero2: '))

# suma =  addTwoNumbers(num1, num2)
# resta = restNumbers(num1, num2)
# multiplicacion = multiplyNumbers(num1, num2)

suma =  calculateResult(num1, num2, 's')
resta = calculateResult(num1, num2, 'r')
multiplicacion = calculateResult(num1, num2, 'm')

print(f'{suma}, {resta} y {multiplicacion}')

