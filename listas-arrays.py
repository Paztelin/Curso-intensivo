#arreglos (arrays, listas)

list  = [1,2,3,4,5,6,7,8,9]
print(list[2:3])#2_3 imprime una posicion

#usando for
for lista in list:
    print(lista, end=" ") #end=" ", es para que imprima de forma horizontal
#\t es para un tab a la derecha
#si ponemos cualquier cosa dentro del print, nos imprime
#el numero de veces que tenemos en el array

"""
Una lista puede contener diferentes tipos de datos:
--> Strings
--> int, double
--> otra lista
--> booleanos
"""
#ejemplo
print('\n')
list2=["Python", 5,10,5, [1, True , 3.89, "martes"], False]
for lista2 in list2:
    print(lista2, end=" ")