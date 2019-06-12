comando = ""

is_start = False
is_stop = False

while True:
    comando = input("> ").lower()
    if comando == "start":
        if is_start:
            print('El auto ya esta encendido')
        else:
            print('El auto encendio')
            is_start = True
    elif comando == 'stop':
        if is_stop:
            print('El auto ya esta apagado')
        else:
            print('El auto esta apagado')
        is_stop = True
    elif comando == 'help':
        print('''
            Start - Enciende el auto
            Stop - Apaga el auto
            Quit - Salir del auto
        ''')
    elif comando == 'quit':
        break
    else:
        print('No entendi tu comando')
