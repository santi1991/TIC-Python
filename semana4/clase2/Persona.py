class Persona:
    def __init__(self, nombre, telefono, correo, documento):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.documento = documento

# herencia de clases
class Vendedor(Persona):
    def __init__(self, nombre, telefono, correo, documento, objetivoVentas, idEmpresarial):
        super().__init__(nombre, telefono, correo, documento)
        self.objetivoVentas = objetivoVentas
        self.idEmpresarial = idEmpresarial
        self.acumuladoVentas = 0
        def acumular(self, monto):
            self.acumuladoVentas = self.acumuladoVentas + monto
        def revisarObjetivo(self):
            if self.acumuladoVentas >= self.objetivoVentas:
                print('el objetivo se ha cumplido')
            else:
                print(f'Aun no se ha cumplido el objetivo. Faltan {self.objetivoVentas - self.acumuladoVentas}')
            print(f'objetivo: {self.objetivoVentas}')
            print(f'acumulado: {self.acumuladoVentas}')

class Cliente(Persona):
    def __init__(self, nombre, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, telefono, correo, documento)        
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion
        self.acumuladoCompra = 0
    def acumular(self, monto):
        self.acumuladoCompra = self.acumuladoCompra + monto

persona1 = Persona('Daniel', '12334', 'asad@c.com', '1234')
persona1 = Persona('Juan', '345', 'bfg@c.com', '8789')