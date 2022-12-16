from random import choice
from time import sleep

print('-=' * 15)
print('JOGO DO JOKENPO')
print('-=' * 15)
sleep(1)

jokenpos = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    pc = choice(jokenpos)
    player = str(input('Escreva pedra, papel ou tesoura para jogar: ').strip().upper())

    if player not in jokenpos:
        print('MENSAGEM INVÁLIDA ')
        sleep(0.5)
    else:
        sleep(0.5)
        print('CARREGANDO ...')
        sleep(0.5)

        print(f'\nPc: {pc.title()}')
        print(f'Você: {player.title()} \n')

        if (player == pc):
            print('EMPATE!')
        elif (player == 'PEDRA' and pc == 'PAPEL') or (player == 'PAPEL' and pc == 'TESOURA') or (player == 'TESOURA' and pc == 'PEDRA'):
            print('VOCÊ PERDEU!!')
        else:
            print('PARABÉNS, VOCÊ GANHOU!!')
        print()
        sleep(0.5)