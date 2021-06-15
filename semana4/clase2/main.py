from Persona import Vendedor
from Tienda import Tienda
from Producto import Producto

nombreTienda = input('ingresa el nombre de la tienda: ')
paginaWeb = input('ingrese la pagina web de la tienda: ')
direccion = input('ingrese direccion de la tienda: ')
tienda = Tienda(nombreTienda, paginaWeb, direccion)


zapatos = Producto('zapatos', 50000)
tienda.agregarProducto(zapatos)
# print(tienda.listaDeProductos[0].nombre)


while True:
    instrucciones = """
        NP agregar un nuevo producto
        I para mostrar todo, 
        V para venta,
        TV mostrar total ventas,
        NV nuevo vendedor
        NC nuevo cliente: 
    """
    operacion = input(instrucciones).upper()
    if operacion == 'NP':
        nombre = input('ingrese nombre del producto: ')
        precio = int(input('ingrese precio del producto: '))
        productoCreado = Producto(nombre, precio)
        tienda.agregarProducto(productoCreado)
        print(f'Se agregó un nuevo producto! {nombre} - ${precio}')
    elif operacion == 'I':
        tienda.mostrarProductos()
    elif operacion == 'V':

        docVendedor = input('Ingrese el documento del vendedor: ')
        vendedorEncontrado = tienda.buscarVendedorPorDocumento(docVendedor)
        
        nombreProducto = input('ingrese nombre producto que quiere comprar: ')
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)


        if not productoEncontrado:
            print('El producto no fue en contrado')
        else:
            cantidadAComprar = int(input('Ingrese la cantidad a comprar: '))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar                
                print(f'venta exitosa, el precio total fue $ {total} pesos')
                productoEncontrado.inventario -= cantidadAComprar
                tienda.totalVentas = tienda.totalVentas + total

                vendedorEncontrado.acumular(total)
                vendedorEncontrado.revisarObjetivo()
                print('_________________________')

                print(f'el total de ventas realizadas: {tienda.totalVentas}')

                vendedorEncontrado.acumular(total)
                vendedorEncontrado.revisarObjetivo()

            else:
                print('no hay inventario suficiente')
    elif operacion == 'TV':
        tienda.mostarTotalVentas()    
    elif operacion == 'NV':
        nombre = input('nombre: ')
        telefono = input('telefono: ')
        correo = input('correo: ')
        documento = input('documento: ')
        objetivo = input('objetivo ventas: ')
        docEmpresarial = input('docEmpresarial: ')
        nuevoVendedor = Vendedor(nombre, telefono, correo, documento, objetivo, docEmpresarial)
        tienda.agregarVendedor(nuevoVendedor)

    else:
        print('operacion incorrecta')