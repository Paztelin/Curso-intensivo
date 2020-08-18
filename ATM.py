""" Hacer un programa que simule un cajero automático con un sueldo inicial de $1000 y tendra el 
siguiente menu de opciones:
1.- Ingresar dinero a la cuenta.
2.- Retirar dinero de la cuenta.
3.- Mostrar dinero disponible.
4.- Salir. """

sueldoin=1000

print("""1.- Ingresar dinero a la cuenta.
2.- Retirar dinero de la cuenta.
3.- Mostrar dinero disponible.
4.- Salir.""")

var=int(input('Deme una opcion a elegir'))
while var!=1 and var!=2 and var!=3 and var!=4:
    var=int(input('Deme una opcion a valida a elegir'))

if var==1:
    ingreso=float(input('Deme el monto a depositar: '))
    sueldoin +=ingreso
    print(f'El sueldo actualizado es {sueldoin}')

elif var==2:
    retiro=float(input('Cuanto desea retirar: '))
    if retiro>sueldoin:
        print('La cantidad a retirar no esta disponible')
    else:
        sueldoin-=retiro
        print(f'El sueldo actual es {sueldoin}')

elif var==3:
    print(f'El sueldo disponible es {sueldoin}')

elif var==4:
    print('Gracias por su preferencia')