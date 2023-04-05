

def povoar():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def pegarElemento(vez):
    return 'X' if vez else 'O'


def marcar(tabuleiro, linha, coluna, el):
    tabuleiro[linha-1][coluna-1] = el
    return tabuleiro


def printar(tabuleiro):
    for lista in tabuleiro:
        for i, item in enumerate(lista):
            print(f'{item}', end="")
            if len(lista)-1 != i:
                print(" | ", end="")

        print("")
    print("----------")


def ganhou(tabuleiro, contPartida, el):

    if contPartida >= 3:

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == el:
            return True
        elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] == el:
            return True
        elif (contPartida == 9):
            return None
        for i in range(len(tabuleiro)):
            contColunas = 0
            contLinhas = 0
            for j in range(len(tabuleiro)):
                if tabuleiro[i][j] == el:
                    contColunas += 1
                if tabuleiro[j][i] == el:
                    contLinhas += 1
            return True if (contLinhas == 3 or contColunas == 3) else False
    else:
        return False


def jogada(tabuleiro, vez, cont):

    el = pegarElemento(vez)
    while True:
        try:
            linha, coluna = map(int, input(
                "Insira sua jogada (linha coluna): ").strip().split(' '))

            while (tabuleiro[linha-1][coluna-1] != ' ' or linha not in [1, 2, 3] or coluna not in [1, 2, 3]):
                if (linha not in [1, 2, 3] or coluna not in [1, 2, 3]):
                    print("Digite somente números entre 1 e 3!")
                else:
                    print("Uma jogada já foi realizada aqui!")
                linha, coluna = map(int, input(
                    "Insira sua jogada (linha coluna)").split(' '))
            break
        except:
            print("Entrada inválida.")

    tabuleiro[linha-1][coluna-1] = el

    return not vez, ganhou(tabuleiro, cont, el)


def jogo():
    vez = True  # true = jogador1, false = jogador2
    jogUm = input("Escreva seu nome, jogador 1: ")
    el = pegarElemento(vez)
    print(f'Você será {el}!')

    jogDois = input("Escreva seu nome, jogador 2: ")
    el = pegarElemento(not vez)
    print(f'Você será {el}!')

    print("Começando!")
    tabuleiro = povoar()

    cont = 0
    seGanhou = False
    while seGanhou != True:
        cont += 1
        vez, seGanhou = jogada(tabuleiro, vez, cont)
        printar(tabuleiro)

        if seGanhou == True:
            vencedor = jogDois if vez else jogUm
            print(f"{vencedor} ganhou!")
        elif seGanhou == None:
            print("Empate!")
            break
