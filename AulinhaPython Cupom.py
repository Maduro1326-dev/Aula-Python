compras = float(input('Digite o valor da sua compra:'))
cupom = ('NIVER10')
desconto = input('Digite o cupom:')
if desconto.upper() == cupom:
    compras = compras * 0.9
    print(f'O valor de suas commpras foi de R$ {compras:.2f}')

elif desconto != cupom:
    print(f'O valor de sua compra foi de R$ {compras:.2f}')





