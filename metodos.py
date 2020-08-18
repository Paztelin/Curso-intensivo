#metodos ----> listas

list=[4,6,9,2,5,10,1,7,3,8] #x2 #duplica la lista
list.sort(reverse=True)
for lista in list:
    print(lista, end=' ')

#list2 = [6,7,8,9,0]
#print(f'La lista tiene {len(list)} elementos') #metodo LEN para saber los arreglos que tiene

#name_lista.append(element)
#ejemplo --->#list.append(6)
#list.insert(2,3)

#list.extend([6,7,8])
#list3=list + list2 #concatena las lista1 y lista2
#print(3 in list) #te dice true o false si el elemento esta en la lista
#print(list.index(4))#nos dice en que posicion esta un elemento

#print(list.count(3))#nos dice cuantas veces se repite un elemento
#list.pop()#elimina el ultimo elemento
#list.pop(3)#elimina un elemento especifico 
#list.remove(1)#elimina un elemento especifico de reverso
#list.clear()#elimina todos los elementos
#list.reverse()#imprime en reversa los elementos
#list.sort()#ordena una lista de manera ascendente
#list.sort(reverse=True)#imprime de mayor a menor una lista en esta pasamos el parametro 'reverse=true'