"""#funcion integrada. Convierte un # a un String
n=str(10)
suma=5+n
print(n)

#convierte un numero a binario:
numero=int(input('Numero: '))
n=bin(numero)
print(n)

#convierte un entero a hexadecimal
numero=int(input('Numero: '))
n=hex(numero)
print(n)

#convierte un binario a un entero
n=int("0b10101010", 2)
print(n)"""


#RECURSIVIDAD
time=int(input('Tiempo we: '))
def atras(seg):
    seg -=1
    if seg > 0:
        print(seg)
        atras(seg)
    else:
        print('Tiempo termina')
atras(time)

