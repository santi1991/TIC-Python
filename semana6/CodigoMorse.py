morse = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
} 

def traductor_a_morse(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    listaPalabras = mensaje_a_traducir.split(' ')
    codigoMorse = ''
    count = 0
    z = 0

    for palabra in listaPalabras:        
        print(f'palabra: {palabra}, longitud: {len(palabra)}')
        print('_____________________________')
        # this is done to avoid the ' /' before the first word
        if count > 0:
            codigoMorse = codigoMorse + ' /'

        for letra in palabra:
            print(letra)
            x = ' '
             # this is done to avoid the ' ' before the first word
            if count == 0 and z == 0:
                z = z + 1
                x = ''            
            codigoMorse = codigoMorse + x + morse[letra]           
        
        count = count + 1
        print('_____________________________')
   
    return codigoMorse
    # return mensaje_traducido

print(traductor_a_morse('NOS HAN PICADO DOS MOSQUITOS'))


# NOS HAN PICADO DOS MOSQUITOS
# -. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ...

# HEMOS ENCONTRADO UNA PLANTA NUNCA ANTES VISTA
# .... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-

# "TENEMOS COMIDA PARA TRES DIAS MAS
# - . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ...