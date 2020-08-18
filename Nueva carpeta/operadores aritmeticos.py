"""Operadores aritmeticos""" #clase type (var)
a=10
b= 12 
c=13
d=10

op=((a>b) or (a<c)) and ((a==c) or (a>=b))
print(op)

"""operadores en asignacion"""
a=5
a+=5 #suma en asignacion
a-=2 #resta en asignacion
a*=3 #multipliacion en asignacion
a/=3 #division en asignacion
a**=2 #potencia en asignacion
a%=2 #modulo en asignacion
print(a)

"""salida de datos"""
nombre='python'
version = 3.7
print(f"curso de {nombre} de version {3.7}")

"""entrada de datos"""
nombre =input('ingrese su nombre')
edad =input('dame tu edad')

print(f'el nombre es{nombre} y la edad es {edad}')

"""suma de numeros"""

num_1=float(input('ingrese un numero'))
num_2=float(input('ingrese otro numero'))

suma = num_1 + num_2
print(suma)