"""
Conjunto ----> lista de elementos desordenados donde
no se puede REPETIR al momento de mandarlo a imprimir, 
los mostrará desordenamente
"""

Conjunto = set() #se inicializa un conjunto vacio

conjunto = {1, 3.5, True, "Hola"} #sus elementos se ponen entre llaves

conjunto.add(3) #'add' para agregar otro elemento al conjunto es asi

conjunto.discard(3.5) #con 'discard' se elimina un elemento

conjunto.clear() #con 'clear' limpiamos el conjunto

print(conjunto)