storedPassword = '123abc'
count = 0
maxRetries = 3
userPassword = input('Ingresa tu clave: ')

while storedPassword != userPassword and count < maxRetries:
    print('las contraseñas no coinciden')
    # count = count + 1
    count += 1
    userPassword = input('Ingresa nuevamente tu clave: ')

if count >= maxRetries:
    print('Dudamos que seas tu, hemos bloqueado tu cuenta')
else:
    print('Hola! bienvenido!!')