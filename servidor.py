import pickle
import info
from socket import *
from random import randint

host = info.host
porta = info.porta

nome_servidor = "Servidor de Carlinhos & Dalva"
num_servidor = randint(1, 100)
# socket é ipv4 e TCP
s = socket(AF_INET, SOCK_STREAM)
# vincula o host a porta
s.bind((host, porta))

# fica ouvindo a porta e esperando o cliente se conectar
s.listen()
print(f" ~~~ [{nome_servidor}] esperando por conexões na porta {porta} ~~~ ")
print(f' Número escolhido pelo servidor: {num_servidor}')

conexao, endereco = s.accept()
print(f"Conectado em {endereco} com sucesso!\n")

# chat
while True:

    # recebe no maximo uma mensagem de 1024 bytes do cliente
    data = conexao.recv(1024)
    nome, num = (pickle.loads(data))

    if (num < 1 or num > 100):
        print("Conexão fechada! Número fora do intervalo\n")
        conexao.sendall(pickle.dumps((nome_servidor, 0)))
        conexao.close()
        break

    print(f'@{nome}: {num} || @{nome_servidor}: {num_servidor}')
    print(f'A soma dos dois números é: {num+num_servidor}!\n')

    # manda de volta pro cliente a tupla em bytes
    conexao.sendall(pickle.dumps((nome_servidor, (num+num_servidor))))
