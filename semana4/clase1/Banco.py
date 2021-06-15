import random
from .Persona import Persona
# ruta y nombre
# hacer una clase que se llame cuenta bancaria
class CuentaBancaria:
    def __init__(self, saldoInicial, personaPropietaria):
        self.numeroCuenta = random.randint(1000, 10000)
        self.saldo = saldoInicial
        self.persona = personaPropietaria
    def retirar(self, monto):
        if monto > self.saldo:
            print('Fondos insuficientes') 
        else:
            self.saldo = self.saldo - monto
            print('Retiro exitoso!')
    def consignar(self, monto):
        if monto > 10000:
            comision = monto * 4 / 1000
            monto = monto - comision
            print(f'la comision por la consignacion es de: {comision}')
            self.saldo = self.saldo + monto
        else:
            self.saldo = self.saldo + monto

        
    def consultarSaldo(self):
        print(f'Cuenta: {self.numeroCuenta}')
        print(f'Saldo: {self.saldo}')
        print(f'_________________')
    

# cuenta = CuentaBancaria(saldoInicial)
listaCuentas = []
listaPersonas = []

def buscarCuentas(mensajeOperacion):
    numCuenta = int(input(f'{mensajeOperacion}: '))
    for cuenta in listaCuentas:
        if cuenta.numeroCuenta == numCuenta:
            print('cuenta encontrada')
            return [True, cuenta]
    return [False]

# def ejecutarOperacion(resultadoBusqueda, operacion):
#     if resultadoBusqueda[0]:
#         cuenta = resultadoBusqueda[1]
#         cuenta.operacion
#     else:
#         print('cuenta no encontrada')

def buscarPersona (cedula, listaDePersonas):
    for persona in listaDePersonas:
        if persona.documento == cedula:
            return persona
    return False

# ciclo que siempre se ejecuta
while True:
    operacion = input('Ingrese N para crear nueva cuenta, S para consultar el saldo, R para retirar, C para consignar: ').upper()
    if operacion == 'N':
        saldoInicial = float(input('Bienvenido al banco XYZ, Para crear su cuenta bancaria, ingrese el saldo inicial: '))

        cedula = input('Ingrese su cedula')
        personaEncontrada = buscarPersona(cedula, listaPersonas)
        if not personaEncontrada:
            # crear una nueva persona
            nuevaPersona = Persona('Daniel', 48, 213213, 'asasd@c.com', 'asdasd', 'Colombiano', 'ingeniero', '1088')
            listaPersonas.append(nuevaPersona)
            # nueva cuenta bancaria y se asocia  la persona 
            nuevaCuenta = CuentaBancaria(saldoInicial, nuevaPersona)
            listaCuentas.append(nuevaCuenta)
        else:
            #crear una nueva cuenta bancaria y asociarla a la persona recientemente creada
            nuevaCuenta = CuentaBancaria(saldoInicial, personaEncontrada)
            listaCuentas.append(nuevaCuenta)
            
        print(f'cuenta creada con exito, el numero de la cuenta es: {nuevaCuenta.numeroCuenta}')
    elif operacion == 'S':       
        busqueda = buscarCuentas('Ingrese la cuenta que desea consultar')
        if busqueda[0]:
            cuenta = busqueda[1]
            cuenta.consultarSaldo()      
        else:
            print('cuenta no encontrada')           
    elif operacion == 'R':
        busqueda = buscarCuentas('Ingrese la cuenta de la que desea retirar')
        if busqueda[0]:
            cuenta = busqueda[1]
            monto = float(input('Ingrese el valor a retirar: '))
            cuenta.retirar(monto)   
        else:
            print('cuenta no encontrada')                 
    elif operacion == 'C':
        busqueda = buscarCuentas('Ingrese la cuenta a la cual quiere consignar')
        if busqueda[0]:
            cuenta = busqueda[1]
            monto = float(input('Ingrese el valor a consignar: '))       
            cuenta.consignar(monto)
            print('Consignacion exitoso!')     
        else:
            print('cuenta no encontrada')          
    else: 
        print('operacion incorrecta')



# EJERCICIO: cobrar una comision del 4 pesos por cada 1000 cuando el monto de la consignacion sea mayor a 10.000
# EJERCICIO; crear una lista de cuentas y agregar la posibilidad de crear o eliminar una cuenta nueva
# cuando se vaya a retirar o consignar, se debe ingresar el numero de la cuenta
# EJERCICIO: crear una clase persona y a la clase cuenta agregarle una persona pidiendole su cedula.
# hay que construir una lista de personas, si la persona no existe