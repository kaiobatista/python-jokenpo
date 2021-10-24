# Pedra, Papel e Tesoura

import random
from time import sleep

opcoes = ['pedra', 'tesoura', 'papel']
running = True

while running:
    pc = random.randint(0, 2)

    # Escolha do jogador
    print(30 * '=')
    while True:
        print('Opções: \n')
        for k, v in enumerate(opcoes):
            print(f'Opção {k + 1} -> {v.capitalize():>5}')
        player = input('\nDigite sua opção:\n>> ').strip().lower()
        if player in opcoes:
            player = opcoes.index(player)
            break
        print('\nOpção inválida!\n')
    sleep(1)

    # Análise do vencedor

    if (pc + 1) % 3 == player:
        player_resultado = 'perdeu'
    elif (player + 1) % 3 == pc:
        player_resultado = 'ganhou'
    else:
        player_resultado = 'empatou'

    # Mensagem final

    print(f'\n\033[34mVocê {player_resultado}!\033[m')
    if player_resultado == 'ganhou':
        print('\033[32mParabéns!\033[m')
    elif player_resultado == 'perdeu':
        print('\033[31mTalvez na próxima...\033[m')

    sleep(2)

    print('\n\n\033[33mDetalhes:')
    print(f'Você: {opcoes[player].capitalize():>11}\nComputador: {opcoes[pc].capitalize():>5}\033[m\n\n\n')
    
    # Reiniciar?

    while True: 
        res = input('Deseja continuar jogando? [S/N]:\n>> ').lower()
        if res == 's':
            print('Certo. Vamos preparar um novo jogo para você...')
            sleep(3)
            break
        elif res == 'n':
            print('Ok. Que pena :(! Estamos fechando o jogo...')
            running = False
            break
        else: 
            print('\033[91m[ERRO] Opção inválida! Por favor, tente novamente.\033[m\n')
