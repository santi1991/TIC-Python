# Paso 1
totalFactura = int(input('Porfavor ingrese valor total factura: '))

# Paso 2: pedirle al usuario el valor que quiere dar de propina
valorPropina = int(input('Porfavor ingrese valor que quiere da rde propina: '))

# Paso 3> hacer el calculo de la propina
propina = totalFactura * valorPropina / 100

# Mostrar al usuario valor propina
print(f'El valor de la propina es {propina} pesos')