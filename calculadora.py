# Interface da calculadora

from calc2 import multiplicacao
from calc2 import soma

# Apresentação
print('\n\t\t\t -- Calculadora 2 --\n')

# Entrada
num1 = int(input('Informe o n1: '))
num2 = int(input('Informe o n2: '))

# Processamento
total = soma(num1, num2)
total = multiplicacao(num1, num2)

# Saída
print(f'{num1} + {num2} = {total}')
print(f'{num1} * {num2} = {total}')
