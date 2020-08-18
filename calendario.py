import calendar

#calendario del año que pidas
"""año = int(input('Ingrese el año: '))
print(f'Calendario del {año}')
print(calendar.calendar(año)) """

#calendario del año y mes que pidas
y= int(input('Que año desea: '))
m=int (input('Que mes desea: '))
print(calendar.month(y, m))