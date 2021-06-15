import random

# (rangoInferior, rangoSuperior)
# print(random.randint(1, 10))

# listOfRandomNumbers = []

# for i in range(0,10):
#     # print(i)
#     listOfRandomNumbers.append(random.randint(1, 100))
# print(listOfRandomNumbers)

def createList(amount, inferiorRange, superiorRange):
    list = []
    for i in range(0, amount):
        list.append(random.randint(inferiorRange, superiorRange))
    return list

def searchNumber(numberToFind, list):
    for i in list:
        found = False
        if i == numberToFind:
            found = True
        return found
        # print(i)

def searchNumber1(numberToFind, list):
    found = False
    for index, element in enumerate(list):
        if element == numberToFind:
            print(f'index {index}, elemento {element}')
            found = True
    return found

randomList = createList(10, 0, 10)
found = searchNumber1(7, randomList)


print(randomList)
print(found)