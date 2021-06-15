import random
# hacer una clase que se llame cuenta bancaria
class CuentaBancaria:
    def __init__(self, saldoInicial):
        self.numeroCuenta = random.randint(1000, 10000)
        self.saldo = saldoInicial
    def retirar(self, monto):
        if monto > self.saldo:
            print('Fondos insuficientes')
        else:
            self.saldo = self.saldo - monto
            print('Retiro exitoso!')
    def consignar(self, monto):
        self.saldo = self.saldo + monto
    def consultarSaldo(self):
        print(f'Cuenta: {self.numeroCuenta}')
        print(f'Saldo: {self.saldo}')
        print(f'_________________')
    
# cuenta1 = CuentaBancaria(10000)
# cuenta1.consultarSaldo()
# cuenta1.retirar(500)
# cuenta1.consultarSaldo()
# cuenta1.consignar(4500)
# cuenta1.consultarSaldo()
saldoInicial = float(input('Bienvenido al banco XYZ, Para crear su cuenta bancaria, ingrese el saldo inicial: '))
cuenta = CuentaBancaria(saldoInicial)
while True:
    operacion = input('S para consultar el saldo, R para retirar, C para consignar: ')
    if (operacion == 'S'):
        cuenta.consultarSaldo()
    elif operacion == 'R':
        monto = float(input('Ingrese el valor a retirar: '))
        cuenta.retirar(monto)
        
    elif operacion == 'C':
        monto = float(input('Ingrese el valor a consignar: '))
        cuenta.consignar(monto)
        print('Consignacion exitoso!')
    else: 
        print('operacion incorrecta')
# EJERCICIO: cobrar una comision del 4 pesos por cada 1000 cuando el monto de la consignacion sea mayor a 10.000
# EJERCICIO; crear una lista de cuentas y agregar la posibilidad de crear o eliminar una cuenta nueva
# cuando se vaya a retirar o consignar, se debe ingresar el numero de la cuenta
# EJERCICIO: crear una clase persona y a la clase cuenta agregarle una persona pidiendole su cedula.
# hay que construir una lista de personas, si la persona no existe