listOfGrades = [
    1,
    2.4,
    4.5,
    2.4,
    4.3,
    3.8,
    3.1,
    3,
    2.7,
    4.5,
    5,
    2.1,
    1.8,
    2.4,
    4.3
]
countI = 0
countA = 0
countS = 0
sumI= 0 
sumA = 0
sumS = 0 

for grade in listOfGrades:
    if grade < 3:
        countI += 1
        sumI = sumI + grade
    elif grade >= 3 and grade < 4:
        countA += 1
        sumA = sumA + grade
    else:
        countS += 1
        sumS = sumS + grade

print(f'promedio insuficiente es {sumI/countI}, contador {countI}')
print(f'promedio aceptable es {sumA/countA}, contador {countA}')
print(f'promedio sobresaliente es {sumS/countS}, contador {countS}')