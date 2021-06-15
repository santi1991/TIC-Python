# Paso 1: pedir el total de la factura
totalFactura = int(input('Ingrese el valor total factura: '))
# Paso 2: pedir el porcentaje de propina que se quiere dar
porcentajePropina = int(input('Ingrese porcentaje propina: '))

# Calcular el valor del iva 19%
valorIva = totalFactura * 19 / 100

# Paso 4: calcular el subtotal  totalFactura - valorIva
subTotal = totalFactura - valorIva

# Paso 5: calcular valor propina  (subtotal * %propina / 100)
valorPropina = subTotal * (porcentajePropina / 100)
#Paso 6: mostrar resultado

print(f'el valor total de la factura fue {totalFactura}')
print(f'el valor del IVA fue {valorIva}')
print(f'el valor del subtotal fue {subTotal}')
print(f'valor de la propina es {valorPropina} pesos')