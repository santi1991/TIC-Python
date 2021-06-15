import math

print(math.pi)


# -----------------------------------------------------------------------
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# -----------------------------------------------------------------------
#  código Python imprimirá los números pares que hay en el intervalo [2, 30]
i = 0
for i in range(2,31,i+2):
    print(i)


# -----------------------------------------------------------------------
# tipo de variable
texto = 'Hola mundo'
print(f'{type(texto)}')

j = 123
type(j)
# <type 'int'>
print(f'{type(j) is int}')
# True
k = 123.456
type(k)
# <type 'float'>

print(f'{type(k) is float}')
# True

# -----------------------------------------------------------------------
#  change the type of the variable  from integer to string on python
num = 5
conv = str(num)
print(f'{type(conv) is str}')

# -----------------------------------------------------------------------
# modo de crear una lista vacía 
a = []
bb = list()
cc = []+[]
list = ['hola', 14, 0.01, ['mundo', 3.14]]
print(list)

# -----------------------------------------------------------------------
# The difference between a tuple and a list is that you cannot change any element from the tuple