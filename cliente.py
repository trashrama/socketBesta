import pickle
import info
from socket import *

host = info.host
porta = info.porta

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, porta))

while True:
    num = input("Insira um número entre 1 e 100: ")

    while not (num.isnumeric()):
        print("Somente números INTEIROS.")
        num = input("Insira um número entre 1 e 100: ")

    # transformo essa tupla em bytes
    data = pickle.dumps((gethostname(), int(num)))
    s.sendall(data)

    servidor, num_novo = pickle.loads(s.recv(1024))
    print(f'@[{servidor}]: {num_novo}')
    if num_novo == 0:
        print('\nConexão encerrada do lado do cliente! (cod 0)')
        s.close()
        break
    print("")
