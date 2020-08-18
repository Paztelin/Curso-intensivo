"""mayor de edad o no"""
"""if anidados"""

edad = int(input('edad: '))

if edad>0 and edad <100: #0<edad<100(opcional)
    print('edad es correcta')
    if edad<18:
        print('es menor de edad')
    if edad >=18:
        print('es mayor de edad')
else:
    print('edad incorrecta')



"""programa si una letra es vocal o no"""
letra = input('dame una letra: ') #.lower() transforma letra mayuscula a minuscula
#.upper() transforma minuscula a mayuscula


if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print(f'la letra es vocal {letra}')
else:
    print(f'la letra es consonante {letra}')