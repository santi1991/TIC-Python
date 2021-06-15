# hacer una clase  que se llama tienda
# 2. los atributos son los siguientes: nombre, pagina web, direccion, listaDeProductos
# from Producto import Producto

class Tienda:
    def __init__(self, nombre, paginaWeb, direccion):
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []
        self.listaDeVendedores = []
        self.totalVentas = 0
    
    def agregarProducto(self, nuevoProducto):
        self.listaDeProductos.append(nuevoProducto)
    
    def mostrarProductos(self):
        for element in self.listaDeProductos:
            print(f'producto: {element.nombre}, inventario: {element.inventario}')
            print('__________________')
    
    def buscarProductoPorNombre(self, productoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == productoABuscar:
                return producto
        return False
    
    def mostarTotalVentas(self):
        print(f'total de ventas es: {self.totalVentas}')    
    
    def agregarVendedor(self, vendedor):
        self.listaDeVendedores.append(vendedor)
    
    def buscarVendedorPorDocumento(self, documento):
        for vendedor in self.listaDeVendedores:
            if vendedor.documento == documento:
                return vendedor
        return False



        

    

