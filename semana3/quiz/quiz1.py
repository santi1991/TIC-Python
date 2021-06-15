# x = int(input("entre un número "))

# y = int(input("entre otro número "))

x = 36
y = 48

z = x % y

print(x, y, end=":", sep=",")

xx = x

yy = y

while z != 0:

    xx = yy

    yy = z

    z = xx % yy

    bb = x * y // yy

print(yy, bb, sep=",")