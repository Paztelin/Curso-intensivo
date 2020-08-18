"""Coleccion----->Diccionario"""

colores={"black": "negro", "golden": "dorado"}
print(colores["black"]) #hacemos referencia a la clave y nos imprime su valor

#para agregar otro elemento:
colores["yellow"]="amarillo"
print(colores)

#para eliminar un elemento:
del(colores["black"])
print(colores)

#ejercicio
equipo={10: "Messi", 11: "Neymar", 7: "Cristiano"}

print(equipo.get(30, 'No existe')) #muestra mensaje que no existe"
print(10 in equipo) #pregunta si el 10 existe en mi conjunto EQUIPO
print(equipo.keys()) #muestra las claves del diccionario, o sea los numeros
print(equipo.values()) #muestra el valor de las claves, o sea los nombres
#print(equipo.items()) #con ITEMS es otra manera de ver los valores por separado

#equipo.clear() #limpia el diccionario
print(len(equipo)) #con LEN sabemos cuantos elementos tiene el diccionario
print(equipo)

