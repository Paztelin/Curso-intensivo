#manda el mensaje
"""def estudiantes():
    print('Hola estudiantes')
estudiantes()"""

#Funcion que muestra la tabla del 7
num = int(input('Numero de la tabla: '))

def tabla7(n):
    for x in range(1,11):
        print(f'{num} x {x} = {num * x}')
tabla7(num)