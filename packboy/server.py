import socket

def filtro(arquivo):
    gamers = {}
    for gamer in arquivo.read().split(","):
      try:
        if gamers[gamer.split(": ")[0].lower()] < gamer.split(": ")[1]:
          gamers[gamer.split(": ")[0].lower()] = gamer.split(": ")[1]
      except KeyError:
        try:
           gamers[gamer.split(": ")[0].lower()] = gamer.split(": ")[1]
        except IndexError or KeyError:
            pass
    resp = ''
    for key in gamers.keys():
      resp += "{0}: {1},".format(key, gamers[key])
    return resp

def enviar(conexao):
    arquivo = open("records.txt", 'r')
    conexao.send(filtro(arquivo).encode("utf-8"))
    arquivo.close()

def adicionar(conexao):
    arquivo = open("records.txt", 'a')
    msg = conexao.recv(1024).decode("utf-8")
    arquivo.write(msg)
    arquivo.flush()
    arquivo.close()

HOST = ''              # Endereco IP do Servidor
PORT = 3333            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
tcp.bind(origem)
tcp.listen(5)
while True:
    print("Esperndo cliente...")
    conexao, cliente = tcp.accept()
    print('Concetado por', cliente)
    requisicao = conexao.recv(1024).decode("UTF-8")
    print(requisicao)
    if requisicao == "set":
        adicionar(conexao)
    elif requisicao == "get":
        enviar(conexao)
    print("Conexao encerrada...")
    conexao.close()
