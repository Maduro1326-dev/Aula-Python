from unidecode import unidecode
valor_bruto = float(input('Insira o valor bruto da viagem: '))
categoria = input('Insira a categoria da viagem (econômica, executiva ou primeira classe): ')
passageiros = int(input('Insira o número de passageiros: '))

# Normaliza (sem acento e minúscula)
categoria = unidecode(categoria.lower())

if categoria == 'economica' and passageiros == 2:
    valor_desconto = valor_bruto * 0.97  # 3% de desconto
    media = valor_desconto / 2
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'economica' and passageiros == 3:
    valor_desconto = valor_bruto * 0.96  # 4% de desconto
    media = valor_desconto / 3
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'economica' and passageiros >= 4:
    valor_desconto = valor_bruto * 0.95  # 5% de desconto
    media = valor_desconto / 4
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'executiva' and passageiros == 2:
    valor_desconto = valor_bruto * 0.95  # 5% de desconto
    media = valor_desconto / 2
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'executiva' and passageiros == 3:
    valor_desconto = valor_bruto * 0.93 # 7% de desconto
    media = valor_desconto / 3
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'executiva' and passageiros >= 4:
    valor_desconto = valor_bruto * 0.92  # 8% de desconto
    media = valor_desconto / 4
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'Primeira classe' and passageiros == 2:
    valor_desconto = valor_bruto * 0.90  # 10% de desconto
    media = valor_desconto / 2
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'Primeira classe' and passageiros == 3:
    valor_desconto = valor_bruto * 0.85  # 15% de desconto
    media = valor_desconto / 3
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')

elif categoria == 'Primeira classe' and passageiros >= 4:
    valor_desconto = valor_bruto * 0.80  # 20% de desconto
    media = valor_desconto / 4
    print(f'O valor bruto de sua viagem foi de R${valor_bruto:.2f} para R${valor_desconto:.2f}, com uma média de R${media:.2f} por passageiro.')
else:
    print(f'Nenhum desconto aplicado. O valor da viagem é R${valor_bruto:.2f}')









