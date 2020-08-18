cola = ['yair', 'carlos', 'emmanuel']

cola.append('paztelin')

n=cola.pop(0)

print(f"Atentiendo a {n}\n ***********************************")
print(f'Favor de esperar {cola} en un momento seran atendidos')


#mismo ejercicio pero diferente codigo
#selecciona a cualquiera de los elementos que tiene la COLA
cola = ['jair', 'carlos', 'emanuel']

cola.append('paztelin')

import random
comienza=random.randint(0, 3)

n=cola.pop(comienza)

print(f'Atentiendo a {n}')
print(cola)