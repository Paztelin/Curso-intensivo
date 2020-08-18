"""escribir un programa que almacene las asignaturas
de un curso (ejemplo: mates, fisica, etc) en una
lista y la muestre por pantalla"""

#ingresa cuantas materias son y el nombre de las materias
list=[]
totalmat=int(input('Cuantas materias son we: '))
for lista2 in range(totalmat):
    nombre=input('escribe la materia: ')
    list.append(nombre)

#muestra las materias ingresadas
print('\n')
for lista2 in list:
    print(f'La materia es: {lista2}')

#pide calificacion de la materia
print('\n')
n=0
sumcal=0
for calif in list:
    calmat=int(input(f'Calificacion de la materia: {list[n]}: '))
    sumcal += calmat
    n+=1
promedio= sumcal/totalmat
print('\n')
print(f'El promedio es: {promedio}')