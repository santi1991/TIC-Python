# function __init__  es el constructor de la clase (siempre recive como argumento -self-)
class Persona:
    def __init__(self):
        self.nombre = 'Daniel'
        self.edad = 67
        self.telefono = 12345
        self.correo = 'abc@c.com'
        self.direccion = 'sdgfg'
        self.nacionalidad = 'colombiano'
        self.profesion = 'ingeniero'
persona1 = Persona()
print(persona1.edad)

class Man:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

man1 = Man('Santiago', 29, 'abc@vv.com')
print(man1.email)