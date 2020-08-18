"""calculadora"""

print("""'INGRESE 1 PARA SUMA'
'INGRESE 2 PARA RESTA'
'INGRESE 3 PARA DIVIDIR'
'INGRESE 4 PARA MULTIPLICAR'""")

var=int(input('\nQUE OPCION QUIERES: '))

while var!=1 and var!=2 and var!=3 and var!=4:
    print('La opcion es invalida')
    var=int(input('\nQUE OPCION QUIERES: '))

num1= float(input('\nDame un numero: '))
num2= float(input('Dame otro numero: '))

if var==1:
    sum=num1 + num2
    print(f"\nLa suma es {sum}")
elif var==2:
    res=num1 - num2
    print(f'\nLa resta es {res}')
elif var==3:
    div=num1/num2
    print(f'\nLa division es {div}')
elif var==4:
    mul= num1*num2
    print(f'\nLa multiplicacion es {mul}')