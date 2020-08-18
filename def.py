list=[]
listpar=[]
listimpar=[]

totdatos=int(input('Dame total de datos que quieres: '))
for n in range(0,totdatos):
    numnuevo=int(input('Dame los valores: '))
    list.append(numnuevo)

def separar(listas):
    for avanzar in list:
        if avanzar %2==0:
            listpar.append(avanzar)
        else:
            listimpar.append(avanzar)
    return listpar, listimpar
listpar,listimpar=separar(list)
print(listpar)
print(listimpar)