import json
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
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []

# logica app ____________________________________________________

tienda = Tienda('Tienda MisionTIC', 'CALLE 123', '321')
# tienda.convertirDiccionarioAProductos()

while True:
    instrucciones = """
        Ingrese P para registrar un nuevo producto:     
        Ingrese IP para imprimir productos de la tienda:
        Ingrese C para registrar un nuevo cliente:   
        Ingrese IC para imprimir clientes de la tienda:
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





