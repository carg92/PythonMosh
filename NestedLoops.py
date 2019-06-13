#(x,y)
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)

#for x in range(4):
#    for y in range(3):
#        print(f'({x},{y})')

#Reto

#Intento #1
#numeros = [5, 2, 5, 2, 2]
#for numero_x in numeros[0:len(numeros)]:
 #   if numero_x == 5:
  #      print('xxxxxx')
   # else:
    #    print('xx')

#Intento #2
#arreglo = [5, 2, 5, 2, 2]
#for x in arreglo[0:len(arreglo):1]:
    #for y in arreglo[0:len(arreglo):1]:
 #   valor_abs = abs(x)
#    print(valor_abs*'x')


#Solución
#array = [5, 2, 5, 2, 2] #F
#for x_count in array:
 #   output = ''
  #  for count in range(x_count):
   #     output += 'x'
    #print(output)




array2 = [2, 2, 2, 2, 5] #L
for x_count2 in array2:
    output2 = ''
    for count2 in range(x_count2):
        output2 += 'x'
    print(output2)
