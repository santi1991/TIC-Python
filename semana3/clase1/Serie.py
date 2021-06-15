# Write a Python program to get the Fibonacci series between 0 to 50. 
# The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

listFibonacci = [0, 1]

count = 1

while len(listFibonacci) < 50:
    listFibonacci.append(listFibonacci[count] + listFibonacci[count-1])
    count+= 1
print(listFibonacci)