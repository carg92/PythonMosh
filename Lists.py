#nombres = ['Cesar', 'Alonso','Romero', 'Garcia']
#print(nombres[:])
#nombres [0] = 'CEsAR'
#print(nombres)


#Ejercicio: Encuentra el número más largo en una lista


#for num in numeros:
 #   print(num)
  #  if num < contador:
   #     contador += num
    #    print(contador)
    #else:
#        print(f'El número: {num} es mayor')
 #       print(contador)

#for opcion in numeros:
 #   print(f'Imprimiendo la opcion: {opcion}')
  #  nueva_lista = opcion
   # if opcion > nueva_lista:
    #    es_mayor = True
     #   print(f'El número {opcion} es mayor')
    #elif opcion < opcion:
     #   es_mayor = False
      #  print(f'El número {opcion} es menor')

numeros = [1, 1231355124, 232, 331313122222124124, 123213509413, 21323449583203320547]
#Solución
max = numeros[0]

for conteo in numeros:
    if conteo > max:
        max = conteo
print(max)







