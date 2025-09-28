
import math

A = int(input('Digite o valor do coeficiente angular: '))
B = int(input('Digite o valor do coeficiente Linear: '))
C = int(input('Digite o valor do termo independente: '))

delta = B*B-4*A*C

print('O valor do delta é de {}'.format(delta))

if delta < 0:
    print('Não há valor real para X')

else:
    x1 = (-B + math.sqrt(delta))/(2*A)
    x2 = (-B - math.sqrt(delta))/(2*A)
    print('Para a equação {}x²+{}x+{} = 0, obtivemos o seguinte valor x1={} e x2={}'.format(A, B, C, x1, x2))



