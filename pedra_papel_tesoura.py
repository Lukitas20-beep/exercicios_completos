repetir = "S"

while repetir == "S":
    jogador1 = int(input("Escolha 0 para pedra, 1 para papel ou 2 para tesoura: "))
    jogador2 = int(input("Escolha 0 para pedra, 1 para papel ou 2 para tesoura: "))
    if 0 <= jogador1 <= 2 and 0 <= jogador2 <= 2:
        if jogador1 == jogador2:
            print("EMPATE")
        elif (jogador1 - jogador2 == 1) or (jogador1 - jogador2 == -2):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
    else:
        print("Opção inválida")

    repetir = input("Digite S para repetir o jogo e N para encerrar ele: ")