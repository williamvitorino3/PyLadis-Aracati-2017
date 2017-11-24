from tkinter import *
from cliente import setter


class Recorde(object):
    def __init__(self, tela, pontos):
        self.tela = tela
        self.pontos = pontos
        self.frame_nome = Frame(self.tela)
        self.label_nome = Label(self.frame_nome, text="Nome")
        self.entry_nome = Entry(self.frame_nome)
        self.entry_nome.bind("<Return>", self.salvar)

        self.frame_pontos = Frame(self.tela)
        self.label_placar = Label(self.frame_pontos, text="Placar: ")
        self.label_valor = Label(self.frame_pontos, text=str(self.pontos))

        self.frame_botao = Frame(self.tela)
        self.botao = Button(self.frame_botao, text="Salvar", command=self.salvar)

        self.frame_nome.pack()
        self.label_nome.pack(side=LEFT)
        self.entry_nome.pack(side=RIGHT)

        self.frame_pontos.pack()
        self.label_placar.pack(side=LEFT)
        self.label_valor.pack(side=RIGHT)

        self.frame_botao.pack()
        self.botao.pack(side=BOTTOM)

    def salvar(self, event=None):
        setter("{0}: {1},".format(self.entry_nome.get(), self.pontos))
        self.tela.quit()
