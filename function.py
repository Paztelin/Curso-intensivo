#recibir por posicion
"""def arg(*a):
    for n in a:
        print(n)
arg('python', 'que hay', 24)"""

#por nombre
def eje(*a, **lo):
    b=0
    for c in a:
        b+=c
    print(b)
    for x in lo:
        print(x, ' ', lo[x])

eje(1,2,3,4, python='lenguage', calif=[9,8,7])