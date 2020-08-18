"""Realiza una funcion llamada relacion con 2 parametros (a,b) que apartir de 2 numeros cumpla lo sig:
*Si el primer numero es mayor que el segundo debe devolver 1*
*Si el primer numero es menor que el segundo debe devolver -1*
*Si ambos numeros son iguales debe devolver un 0*

num1=int(input('Dame un numero: '))
num2=int(input('Dame otro numero: '))

def relacion(a,b):
    if num1>num2:
        return 1
    
    elif num1<num2:
        return -1
    
    elif num1==num2:
        return 0

print(relacion(num1,num2))"""


""" Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite 
superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite. """

num1=int(input('Dame un numero: '))
num2=int(input('Dame otro numero: '))
num3=int(input('Otro numero: '))

def recortar(num,min,max):
    if num < min:
        return print(f"El limite inferior es: {min}")

    elif num>max:
        return print(f'El limite exterios es: {max}')

    return print(f'No existe ningun limite: {num}')

resultado=recortar(num1,num2,num3)

print(resultado)