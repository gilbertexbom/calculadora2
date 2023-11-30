# Interface da calculadora

from Gilbcalc2 import divi
from Gilbcalc2 import multi

# Apresentação
print('\n\t\t\t -- Gilbertdivi --\n')

# Entrada
num1 = int(input('Informe o n1: '))
num2 = int(input('Informe o n2: '))

# Processamento
total = divi(num1, num2)

# Saída
print(f'{num1} + {num2} = {total}')

print('\n\t\t\t -- Gilbertmulti --\n')

num3 = int(input('Informe o n3: '))
num4 = int(input('Informe o n4: '))

total2 = multi(num3, num4)

print(f'{num3} + {num4} = {total2}')

print('\n\t\t\t -- Gilbertsoma --\n')

total3 = total + total2

print(f'{total} + {total2} = {total3}')

