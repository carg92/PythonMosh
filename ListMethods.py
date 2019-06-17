


#numbers.append(20)
#numbers.insert(0,10)
#numbers.remove(5)
#print(numbers)
#numbers.clear()
#obtener_num = numbers.pop(2)
#print(numbers)
#numbers.sort()
#numbers.reverse()
#numbers2 = numbers.copy()
#numbers.append(12)
#print(numbers)
#print(numbers2)
#Ejercicio
conteo = 0
numbers = [5,2,5,8,0,9,2,1,5,7,4,4]
numbers.sort()

for numero in numbers:
    conteo = numbers.count(numero)
    print(f'El número: {numero} aparece: {conteo} veces en la lista')
    if numbers.count(numero) > 1:
        numbers.remove(numero)
        print(f'El número: {numero} ha sido eliminado de la lista')
    else:
        print(f'El número: {numero} aparece: {conteo} veces en la lista')
print(numbers)




