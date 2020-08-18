while True:
    print("""
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir""")

    opcion=int(input('Que opcion quieres: '))

    if opcion>=1 and opcion<=4:
        print('Ingrese dos numeros: ')
        num1=float(input())
        num2=float(input())

        if opcion ==1:
            res= num1 + num2
            print(f'La suma es: {res}')
        
        elif opcion ==2:
            res= num1 - num2
            print(f'La resta es: {res}')

        elif opcion ==3:
            res= num1 * num2
            print(f'La multiplicacion es: {res}')

        else:
            res = num1/num2
            print(f'La division es: {res}')

        exit()

    else:
        print('Bye')