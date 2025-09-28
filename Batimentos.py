idade = int(input('Insira sua idade:'))
batimentos = int(input('Insira os batimentos por minuto(BPM):'))

if idade <=2 and 120 <= batimentos <= 140:
    print('O seu batimento cardíaco está dentro do padrão')

elif 8 <= idade <= 17 and 80 <= batimentos <= 100:

    print('O seu batimento cardíaco está dentro do padrão')

elif 17 <= idade <= 60 and 70 <= batimentos <= 80:
    print('O seu batimento cardíaco está dentro do padrão')


elif idade > 60 and 50 <= batimentos <= 60:
    print('O seu batimento cardíaco está dentro do padrão')

else:
    print('Seu batimento cardíaco está fora do padrão')









