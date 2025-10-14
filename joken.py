from random import randint  # Importa a função que gera números aleatórios

# Tupla com as opções possíveis do jogo
itens = ('Pedra', 'Papel', 'Tesoura')

# O computador escolhe um número aleatório entre 0 e 2
computador = randint(0, 2)

# Mostra as opções pro jogador
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

# Pede a jogada do jogador
jogador = int(input('Qual é a sua jogada? '))

print('-=' * 15)
print(f'O adversario jogou: {itens[computador]}')
print(f'Você jogou: {itens[jogador]}')
print('-=' * 15)

# Regras do jogo
if computador == jogador:
    print('Empate!')
elif (computador == 0 and jogador == 1) or \
     (computador == 1 and jogador == 2) or \
     (computador == 2 and jogador == 0):
    print('Você venceu!')
elif jogador > 2 or jogador < 0:
    print('Jogada inválida! Tente novamente.')
else:
    print('Adversario venceu!')
