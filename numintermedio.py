"""Realiza una funcion llamada intermedio(a,b) que a partir
de 2 numero, devuelva su punto intermedio. Cuando lo tengas
comprueba el punto intermedio entre -12 y 24"""

num1=int(input('Numero 1: '))
num2=int(input('Numero 2: '))

def intermedio(a,b):
    return (a+b)/2

result = intermedio(num1,num2)
print(f'El numero intermedio es: {result}')