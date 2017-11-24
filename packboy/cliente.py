# -*- coding: utf-8 -*-

# #################################
# ###### WV Desenvolvimentos ######
# #################################

import socket


def setter(txt):
    sock = conectar()
    sock.send("set".encode("utf-8"))
    sock.send(txt.encode("utf-8"))
    sock.close()


def getter():
    sock = conectar()
    sock.send("get".encode("utf-8"))
    placar = sock.recv(1024).decode("utf-8").split(",")
    sock.close()
    return placar


def conectar():
    maquina = '127.0.0.1'       # Endereco IP do Servidor
    porta = 3333                # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor = (maquina, porta)
    tcp.connect(servidor)
    return tcp
