# Interface da calculadora

from calc2 import mult
from calc2 import soma
from calc2 import sub

# Apresentação
print('\n\t\t\t -- Calculadora 2 --\n')

print('\n\t -- Soma --\n')

# Entrada
num1 = int(input('Informe o n1: '))
num2 = int(input('Informe o n2: '))

print('\n\t -- Resultado da Soma --\n')

# Processamento
total = soma(num1, num2)

# Saída
print(f'{num1} + {num2} = {total}')

# Proxima operação
print('\n\t -- Multiplicação --\n')

# Entrada
num3 = int(input('Informe o n1: '))
num4 = int(input('Informe o n2: '))

print('\n\t -- Resultado da Multiplicação --\n')

# Processamento
total2 = mult(num3, num4)

# Saída
print(f'{num3} * {num4} = {total2}')

# Proxima operação
print('\n\t -- Subtração --\n')

# Entrada
num5 = int(input('Informe o n1: '))
num6 = int(input('Informe o n2: '))

print('\n\t -- Resultado da Subtração --\n')

# Processamento
total3 = sub(num5, num6)

# Saída
print(f'{num5} - {num6} = {total3}')

