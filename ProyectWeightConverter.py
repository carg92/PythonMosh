peso = input('¿Cual es tu peso? ')
lb_kg = input('¿En (L)ibras o (K)ilogramos? ')

convertir_peso = int(peso)

if lb_kg.upper() == 'L':
    print('Pesas ', convertir_peso*0.45, ' Kilogramos')
elif lb_kg.upper() == 'K':
    print('Pesas ', convertir_peso*2.20, ' Libras')

