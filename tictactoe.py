def povoar():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def printar(tabuleiro):
    for lista in tabuleiro:
        for i, item in enumerate(lista):
            print(f'{item}', end="")
            if len(lista)-1 != i:
                print(" | ", end="")

        print("")
    print("----------")


def ganhou(tabuleiro):

    contColunas = 0
    contLinhas = 0

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == 'X':
                contColunas += 1
            if tabuleiro[j][i] == 'X':
                contLinhas += 1

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
        print('venceu')
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] == 'X':
        print('venceu')
    elif (contColunas == 3):
        print('venceu')
    elif (contLinhas == 3):
        print('venceu')
    else:
        print('empate')


print("JOGAR")
# nome = input("Escreva seu nome 1")

tabuleiro = povoar()
printar(tabuleiro)
tabuleiro[0][2] = 'X'
tabuleiro[1][1] = 'X'
tabuleiro[2][0] = 'X'

printar(tabuleiro)
ganhou(tabuleiro)
