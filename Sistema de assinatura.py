assinatura = input('Digite sua assinatura (Basic, silver, gold e platinum):')
faturamento = float(input('Digite sua faturamento anual: '))

if assinatura.lower() == 'basic':
        liquido = faturamento * 0.7 #30% de desconto
        print(f'O valor que você vai pagar conforme seu plano será de {liquido:}')

elif assinatura.lower() == 'silver':
        liquido = faturamento * 0.8 #20% de desconto
        print(f'O valor que você vai pagar conforme seu plano será de {liquido:}')
elif assinatura.lower() == 'gold':
        liquido = faturamento * 0.9 #10% de desconto
        print(f'O valor que você vai pagar conforme seu plano será de {liquido:}')
elif assinatura.lower() == 'platinum':
        liquido = faturamento * 0.95 #5% de desconto
        print(f'O valor que você vai pagar conforme seu plano será de {liquido:}')

else:
        print('Assinatura inválida! Digite Basic, Silver, Gold ou Platinum.')










