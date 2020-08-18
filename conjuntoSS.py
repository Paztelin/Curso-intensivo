#conjuntos
a = {1,2,3}
#se puede omitir el SET poniendo llaves{}
b={3,4,5}

#UNION de conjuntos
#al mostrar en pantalla mostrara los elementos que no se repitan
#por tal razon tomo el elemento del conjunto A y B 

#lo emite
c = a | b
print(c)
#INTERSECCION de conjuntos
d = a & b
d=(d)
#DIFERENCIA de conjuntos
e= a-b
print(e)
#DIFERENCIA simetrica
f = a ^ b
print(f)
#saber si un conjunto es subconjunto de otro
#en este caso el primer conjunto que esta en
#la linea 2
g= {1,2,3,4,5,}
print(a.issubset(g))