import pickle
import info
from socket import *
from random import randint
from threading import Thread, active_count
from tictactoe import *
from time import sleep

jogadores = []


def funcaoJogo(conexao):
    global jogadores
    tabuleiro = povoar()
    jogadores.append(conexao)

    while len(jogadores) != 2:
        pass

    vez = True  # true jogador 1 false jogador 2

    while True:
        jogadorDaVez = jogadores[0] if vez else jogadores[1]
        if jogadorDaVez == jogadores[0]:
            print("eh o 0")
        if jogadorDaVez == jogadores[1]:
            print("eh o 1")

        if jogadorDaVez == jogadores[0]:
            jogadores[0].send(pickle.dumps(
                (tabuleiro, True)))
            jogadores[1].send(pickle.dumps(
                (tabuleiro, False)))
        else:
            jogadores[1].send(pickle.dumps(
                (tabuleiro, True)))
            jogadores[0].send(pickle.dumps(
                (tabuleiro, False)))

        l, c = pickle.loads(jogadorDaVez.recv(4096))
        print(l, c)
        tabuleiro = marcar(tabuleiro, l, c, pegarElemento(vez))
        printar(tabuleiro)

        vez = not vez


host = info.host
porta = info.porta

nome_servidor = "Servidor de Carlinhos & Dalva"
# socket é ipv4 e TCP
s = socket(AF_INET, SOCK_STREAM)
# vincula o host a porta
s.bind((host, porta))

# fica ouvindo a porta e esperando o cliente se conectar
s.listen()

ativo = True  # ta ativo o servidor

while ativo:
    conexao, endereco = s.accept()

    Thread(target=funcaoJogo, args=(
        conexao, )).start()

    if (active_count()-1 == 0):
        ativo = False
s.close()
