operaciones_usuario = [
    'Definamos qué es una función de Python: ', 
    'Una función es ', 
    'un arregrlo unidimensional de datos', 
    'DESHACER', 
    'DESHACER', 
    'REHACER', 
    'un grupo de instrucciones'
]

def actualizar_estado_editor(operaciones_usuario):
    texto_escrito = []
    rehacer = []
    texto_actual = ''
    cont = 0
    for texto in operaciones_usuario:
        if texto == 'DESHACER':
            rehacer.append(texto_actual)
            texto_actual = texto_escrito.pop()
        elif texto == 'REHACER':
            texto_escrito.append(texto_actual)
            texto_actual = rehacer.pop()
        else:                              
            if cont > 0:                
                texto_escrito.append(texto_actual)                
            texto_actual = texto
            cont = cont + 1  

    cadena_final = ''
    for i in texto_escrito:
        cadena_final = cadena_final + i
            
    cadena_final = cadena_final + texto_actual   

    return cadena_final 

print(actualizar_estado_editor(operaciones_usuario))