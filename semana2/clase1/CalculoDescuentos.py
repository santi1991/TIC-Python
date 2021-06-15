# precio base de los huevos 1.800
# precio base de las arepas 5.000
# si alguien compra mas de 10 canastas, el precio base 1.000

# si alguien compra mas de 10 canastasd de huevos y ademas compra 10 paquetes de arepas
# el precio huevos 800 y de arepas 2000

# paso 1 preguntar cuantos huevos quiere comprar la persona
cantidadHuevos = int(input('Digite la cantidad de canastas de huevos que quiere comprar: '))
# paso 2 preguntar si la persona quiere arepas
quiereArepas = input('usted desea llevar arepas?: ').lower()
cantidadArepas = 0
# paso 3 si quiere arepas, preguntar cuantas
if quiereArepas == 'si':
    cantidadArepas = int(input('Digite la cantidad de paquetes de arepas que quiere comprar: '))

# calcular total

if cantidadArepas > 10 and cantidadHuevos > 10:
    precioHuevos = 800
    precioArepas = 2000
elif cantidadHuevos > 10:
    precioHuevos = 1000
    precioArepas = 5000
else:
    precioHuevos = 1800
    precioArepas = 5000

subTotal = precioHuevos * cantidadHuevos + precioArepas * cantidadArepas
print(f'precio huevo {precioHuevos}, preciero arepa {precioArepas}')
print(f'El subtotal de su compra es {subTotal}')

if subTotal > 50000 and (cantidadHuevos == 0 or cantidadArepas == 0):
    descuento = subTotal * 10 / 100
    totalFinal = subTotal - descuento
    print(f'El descuento de la compra es de {descuento} pesos')
    print(f'el total final de la compra es {totalFinal} pesos')
elif subTotal > 50000 and (cantidadHuevos > 0 or cantidadArepas > 0):
    descuento = subTotal * 15 / 100
    totalFinal = subTotal - descuento
    print(f'El descuento de la compra es de {descuento} pesos')
    print(f'el total final de la compra es {totalFinal} pesos')

# condiciones adicionales que se deben cumplir
# if totalCompra > 50000: y solo comprando un producto hacer descuento de 10%
# if totalCompra > 50000:  y ademas se estan comprando huevos y arepas, hacer descuento de 15%

# mostrar total compra y total descuento
    