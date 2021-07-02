import json
import csv
#1. crear una clase Tienda que tenga los siguientes atributos:
    #nombre
    #direccion
    #telefono
    #lista de productos
    #lista de clientes
    #histórico de ventas
class Tienda:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []
        self.clientes = []
        self.ventas = []
        # definir metodo para agregar un nuevo producto
    def agregarProducto(self, producto):
        self.productos.append(producto)
    def imprimirProductos(self):
        for producto in self.productos:
            print(producto)
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def imprimirClientes(self):
        for cliente in self.clientes:
            print(cliente)
    def convertirProductosADiccionario(self):
        diccProductos={"productos":[]}
        for producto in self.productos:
            # diccProductos["productos"].append({"nombre":producto.nombre,"precio":producto.precio})
            diccProductos["productos"].append(producto.__dict__)
        with open('productos.json','w') as jsonFile:
            json.dump(diccProductos,jsonFile)
            jsonFile.close()

    def convertirDiccionarioAProductos(self):
        with open('productos.json') as jsonFile:
            diccionarioProductos = json.load(jsonFile)
            jsonFile.close()
        for producto in diccionarioProductos["productos"]:
            nuevoProducto = Producto(producto["nombre"],producto["precio"])
            self.productos.append(nuevoProducto)

    def convertirClientesADiccionario(self):
        diccClientes={"clientes":[]}
        for cliente in self.clientes:
            # diccProductos["productos"].append({"nombre":cliente.nombre,"documento":cliente.documento})
            diccClientes["clientes"].append(cliente.__dict__)
        with open('clientes.json','w') as jsonFile:
            json.dump(diccClientes,jsonFile)
            jsonFile.close()

    def convertirDiccionarioAClientes(self):
        with open('clientes.json') as jsonFile:
            diccClientes = json.load(jsonFile)
            jsonFile.close()
        for cliente in diccClientes["clientes"]:
            nuevoCliente = Producto(cliente["nombre"],cliente["documento"])
            self.clientes.append(nuevoCliente)

    def buscarProducto(self, nombreProducto):
        for producto in self.productos:
            if producto.nombre == nombreProducto:
                return producto
        return False

    def buscarCliente(self, documento):
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente
        return False

    def agregarVenta(self, venta):
        self.ventas.append(venta)
        self.convertirVentasACSV()

    def imprimirVentas(self):
        for venta in self.ventas:
            print(venta)

    def convertirVentasACSV(self):
        diccVentas = []
        columnas = ["fecha","cliente","producto","cantidad"]
        for venta in self.ventas:
            diccVentas.append({"fecha":venta.fecha,"cliente":venta.cliente.documento,"producto":venta.producto.nombre,"cantidad":venta.cantidad})
        # print(diccVentas)
        with open('ventas.csv','w') as csvFile:
            writer = csv.DictWriter(csvFile,columnas)
            writer.writeheader()
            writer.writerows(diccVentas)


#2. crear una clase Producto que tenga los siguientes atributos:
    #nombre
    #precio
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return self.nombre + ' - ' + str(self.precio)
        

#3. crear una clase Cliente que tenga los siguientes atributos:
    #nombre
    #documento
    #lista de compras
class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        self.compras = []    
    def __str__(self):
        return self.nombre + ' - ' + self.documento

#4. crear una clase Venta que tenga los siguientes atributos:
    #fecha
    #lista de productos y cantidades
    #cliente
class Venta:
    def __init__(self, cliente, fecha, producto, cantidad):
        self.cliente = cliente
        self.fecha = fecha
        self.producto = producto
        self.cantidad = cantidad
    def __str__(self):
        return self.cliente.documento + " - " + self.producto.nombre + " - " + str(self.cantidad)

# logica app ____________________________________________________

tienda = Tienda('Tienda MisionTIC', 'CALLE 123', '321')

try:
    tienda.convertirDiccionarioAProductos()    
except:
    print('No existe el archivo de producto, Inicializando desde cero')

try:
    tienda.convertirDiccionarioAClientes()
except:
    print('No existe el archivo de clientes, Inicializando desde cero')


while True:
    instrucciones = """
        Ingrese P para registrar un nuevo producto:     
        Ingrese IP para imprimir productos de la tienda:
        Ingrese C para registrar un nuevo cliente:   
        Ingrese IC para imprimir clientes de la tienda:
        Ingrese V para generar una venta:
        Ingrese IV para imprimir las ventas:
    """
    operacion = input(instrucciones).upper()
    if operacion == 'P':
        nombre = input('ingrese nombre del producto: ')
        precio = float(input('ingrese precio del producto: '))
        nuevoProducto = Producto(nombre, precio)
        tienda.agregarProducto(nuevoProducto)
    elif operacion == 'IP':
        tienda.imprimirProductos()
        tienda.convertirProductosADiccionario()
    elif operacion == 'C':
        nombre = input('ingrese nombre del cliente: ')
        documento = input('ingrese documento del cliente: ')
        nuevoCliente = Cliente(nombre, documento)
        tienda.agregarCliente(nuevoCliente)
    elif operacion == 'IC':
        tienda.imprimirClientes()
        tienda.convertirClientesADiccionario()
    elif operacion == "V":
        nombreProducto = input("ingrese el nombre del producto: ")
        productoEncontrado = tienda.buscarProducto(nombreProducto)
        print(productoEncontrado)
        documentoCliente = input("ingrese el documento del cliente: ")
        clienteEncontrado = tienda.buscarCliente(documentoCliente)
        print(clienteEncontrado)
        cantidad = input("Ingrese la cantidad de producto que desea comprar: ")
        nuevaVenta = Venta(clienteEncontrado,"30/06/2021",productoEncontrado,cantidad)
        tienda.agregarVenta(nuevaVenta)
    elif operacion == "IV":
        tienda.imprimirVentas()





