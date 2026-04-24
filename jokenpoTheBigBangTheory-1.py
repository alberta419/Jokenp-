from random import randint
opcao = 0
cont_p1 = 0
cont_p2 = 0
cont_empate = 0
partidas_realizadas = 0

print("Bem-vindo ao Jokenpô The Big Bang Theory! Neste jogo, você pode escolher entre: pedra, papel e tesoura. Veja as interações:")
print("- Tesoura corta o papel")
print("- Papel cobre a pedra")
print("- Pedra mata a tesoura")
print("Faça sua escolha e boa sorte!")

while opcao != 5:

    print("\nPara jogar, escolha uma das opções abaixo:\n" \
    "1. Modo Humano x Humano\n" \
    "2. Modo Humano x computador\n" \
    "3. Modo computador x computador\n" \
    "4. Estatísticas\n" \
    "5. Sair\n")
    opcao = int(input("Opção escolhida: \n"))

    if opcao == 1:
        jogador = int(input("\nJogador 1, escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))
        jogador_2 = int(input("\nJogador 2, escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))

        if jogador == jogador_2:
            print("\nEmpate\n")
            partidas_realizadas = partidas_realizadas + 1
            cont_empate = cont_empate + 1
        elif (jogador == 1 and jogador_2 == 3) or \
            (jogador == 2 and jogador_2 == 1) or \
            (jogador == 3 and jogador_2 == 2) or \
            print("\nJogador 1 venceu\n"):
            cont_p1 = cont_p1 + 1
            partidas_realizadas = partidas_realizadas + 1
        else:
            print("\nJogador 2 venceu\n")
            cont_p2 = cont_p2 + 1
            partidas_realizadas = partidas_realizadas + 1

    elif opcao == 2:
        jogador = int(input("\nJogador 1, escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura: "))

        jogada_computador = randint(1,3)
        print("Número escolhido pelo computador: ",jogada_computador)

        if jogador == jogada_computador:
            print("\nEmpate\n")
            partidas_realizadas = partidas_realizadas + 1
            cont_empate = cont_empate + 1
        elif (jogador == 1 and jogada_computador == 3) or \
            (jogador == 2 and jogada_computador == 1) or \
            (jogador == 3 and jogada_computador == 2) or \
            print("\nJogador 1 venceu\n"):
            cont_p1 = cont_p1 + 1
            partidas_realizadas = partidas_realizadas + 1
        else:
            print("\nJogador 2 venceu\n")
            cont_p2 = cont_p2 + 1
            partidas_realizadas = partidas_realizadas + 1

    elif opcao == 3:
        jogada_computador = randint(1,3)
        print("\nNúmero escolhido pelo computador 1: ",jogada_computador)

        jogada_computador2 = randint(1,3)
        print("\nNúmero escolhido pelo computador 2: ",jogada_computador2)

        if jogada_computador == jogada_computador2:
            print("\nEmpate\n")
            partidas_realizadas = partidas_realizadas + 1
            cont_empate = cont_empate + 1
        elif (jogada_computador == 1 and jogada_computador2 == 3) or \
            (jogada_computador == 2 and jogada_computador2 == 1) or \
            (jogada_computador == 3 and jogada_computador2 == 2) or \
            print("\nJogador 1 venceu\n"):
            cont_p1 = cont_p1 + 1
            partidas_realizadas = partidas_realizadas + 1
        else:
            print("\nJogador 2 venceu\n")
            cont_p2 = cont_p2 + 1
            partidas_realizadas = partidas_realizadas + 1

    elif opcao == 4:
        percentual_vitorias_p1 = (cont_p1 / partidas_realizadas) * 100
        percentual_vitorias_p2 = (cont_p2 / partidas_realizadas) * 100
        print("Aqui estão as estatísticas:\n")
        print("\nPercentual de vitórias do Jogador 1: ", percentual_vitorias_p1)
        print("\nPercentual de vitórias do Jogador 2: ", percentual_vitorias_p2)
        print("\nVezes que resultou em Empate: ", cont_empate)
        print("\nPartidas jogadas: ", partidas_realizadas)

    elif opcao == 5:
        print("\nSaindo! Obrigado por jogar. Feito por: Pedro Henrique Hara Bialy e Yasmim Egidio.")

    else:
        print("Opção inválida. Tente novamente.")


#Código realizado por:  Pedro Henrique Hara Bialy e Yasmim Egidio
