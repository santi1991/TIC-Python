#implementar un sistema de gestión de tareas
#un usuario debe tener un nombre, una lista de tareas y una tarea en curso
#los elementos de la lista de tareas son de una clase Tarea
#la clase Tarea tiene los siguientes atributos:
    #descripción de la tarea
    #fecha límite de la tarea
#la clase usuario tiene los siguientes atributos:
    #nombre
    #tareaActual
    #listaTareas
#la clase usuario tiene los siguientes métodos:
    #agregar una tarea:
        #si el usuario no tiene tarea actual, la agrega como tarea actual
        #si el usuario ya tiene tarea actual, la agrega a la lista de tareas pendientes
    #finalizar una tarea
        #saca la siguiente tarea de la lista y la pone en "tarea actual".

#1. Hacer clase tarea
class Task:
    def __init__(self, description, dueDate):
        self.description = description
        self.dueDate = dueDate
    def __str__(self):
        return self.description + ' - ' + self.dueDate
        
# Hacer clase usuario
class User:
    def __init__(self, name):
        self.name = name
        self.currentTask = ''
        self.taskList = []
    def addTask(self, newTask):
        # revisar si el usuario ya tiene una 'tarea actual'
        if self.currentTask == '':
            self.currentTask = newTask
        else:
            self.taskList.append(newTask)

    def printTasks(self):
        print("tarea actual",self.currentTask)
        print("lista de tareas: ")
        for task in self.taskList:
            print(task)

    def endTask(self):
        if len(self.taskList) > 0:
            self.currentTask = self.taskList.pop(0)
        else:
            self.currentTask = ''
            
#hacer logica de la aplicacion

user = User('Daniel')

while True:
    operaciones = """
        Ingrese A para registrar una nueva tarea
        Ingrese F para finalizar la tarea actual
        Ingrese I para imprimir la lista de tareas:       
    """
    inputUsuario = input(operaciones).upper()

    if inputUsuario == 'A':
        description = input('Ingresa la descripción de la tarea: ')
        dueDate = input('Ingresa la fecha limite: ')
        newTask = Task(description, dueDate)
        user.addTask(newTask)
        #pedir al usuario la descripcion de la tarea y la fecha limite
        #crear la nueva tarea
        #implementar el metodo addTask de la clase User
        print('agregar una nueva tarea')
    elif inputUsuario == 'F':
        user.endTask()
        print('Finalizar la tarea actual')
    elif inputUsuario == 'I':
        user.printTasks()