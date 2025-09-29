from unidecode import unidecode
#Criando o armazenamento(variável)
playstation = 0
xbox = 0
nintendo = 0

print('As opções são PLAYSTATION, XBOX E NINTENDO')

for membro in range(1,6):
    voto = input(f'Digite aqui o voto do membro {membro}:')
    voto = unidecode(voto).lower()

#armazenamento dos votos
    if voto == 'playstation':
        playstation += 1

    elif voto == 'xbox':
        xbox += 1

    elif voto == 'nintendo':
        nintendo += 1

    else:
        print('Seu voto está errado')

#verificando qual ganhou

if playstation > xbox and playstation > nintendo:
        print(f'O videogame mais votado foi o Playstation com {playstation} votos.')

elif xbox > playstation and xbox > nintendo:
        print(f'O videogame mais votado foi o xbox com {xbox} votos.')

elif nintendo > xbox and nintendo > playstation:
        print(f'O videogame mais votado foi o nitendo com {nintendo} votos.')

else:
        print('Houve empate na votação, será necessário outro sorteio!')




















