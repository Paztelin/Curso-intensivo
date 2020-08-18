"""calcular el area y longitud de un circulo
area = pi *radio^2
longitud = 2* pi* radio"""

radio = float(input('ingrese el radio: '))
pi=3.1416
op1 = pi*radio*radio
op2 = 2*pi*radio
print(f'el area es {op1:.3f} y la longitud es {op2:.3f}') 

"""sentencia if"""

numero = int(input('numero: '))

if numero>0:
    print('el numero es positivo')
elif numero==0:
    print('el numero es cero')
else:
    print('el numero es negativo')