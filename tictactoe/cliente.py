import pickle
import info
from time import sleep
from tictactoe import *
from socket import *


def jogar(s):
    while True:

        tabuleiro, minhaVez = pickle.loads(s.recv(10240))
        printar(tabuleiro)

        if minhaVez == True:
            try:
                linha, coluna = map(int, input(
                    "Insira sua jogada (linha coluna): ").strip().split(' '))

                while (tabuleiro[linha-1][coluna-1] != ' ' or linha not in [1, 2, 3] or coluna not in [1, 2, 3]):
                    if (linha not in [1, 2, 3] or coluna not in [1, 2, 3]):
                        print("Digite somente números entre 1 e 3!")
                    else:
                        print("Uma jogada já foi realizada aqui!")
                        linha, coluna = map(int, input(
                            "Insira sua jogada (linha coluna)").strip().split(' '))

                print("enviando jogada...")
                s.send(pickle.dumps((linha, coluna)))
            except:
                print("Entrada inválida.")

        elif minhaVez == False:
            print("Aguardando jogada do adversário...")
            while True:
                tabuleiro, minhaVez = pickle.loads(s.recv(10240))
                if minhaVez == True:
                    break
                sleep(1)  # espera 1 segundo antes de checar novamente

        if minhaVez == True:
            print("Sua vez de jogar. Aguarde a jogada do adversário...")
        else:
            print("Jogada do adversário recebida. Aguarde sua vez de jogar...")


host = info.host
porta = info.porta

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, porta))

    print("Procurando jogador...")
    jogar(s)

    s.close()
    break

print('terminou')
