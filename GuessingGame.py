secreto = 9
intentos = 0

intentos_max = 3


while intentos < intentos_max:
    adivinar = int(input('Dime un número... '))
    intentos = intentos + 1
    if adivinar == secreto:
        print(f"Has adivinado el número secreto {secreto}")
        break
else:
    print('Has fallado')


