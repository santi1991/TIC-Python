
clavesIguales = False
while clavesIguales == False:
    clave1 = input('ingrese tu clave: ')
    clave2 = input('repite tu clave: ')
    if (clave1 == clave2):
        clavesIguales = True
    else:
        print('Las claves son diferentes')

print('te has registrado!')