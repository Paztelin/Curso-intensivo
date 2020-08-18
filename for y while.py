#tablas multiplicar con range

numero=int(input('Ingrese un numero: '))
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')

#tabla multiplicar con variable
print('\n')
numero=int(input('Ingrese un numero: '))
mul=int(input('Limite a multiplicar: '))
for i in range(1,mul+1):
    print(f'{numero} x {i} = {numero * i}')

#sumar 10 numeros
print('\n')
suma=0
for n in range(0,10):
    numero=int(input('Ingrese numero: '))
    suma= suma + numero
print(f'La suma es: {suma}')

#numeros pares dado el rango que queramos  
print('\n')
num1=int(input('Dame primer numero: '))
num2=num1
while num2<=num1:
    num2=int(input('Dame otro numero mayor al primer numero: '))

for n in range(num1,num2+1):
    if n %2==0:
        print(n)