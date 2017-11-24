from tkinter import *
from cliente import getter


class ListaPontos(object):
    def __init__(self):
        self.resposta = False
        self.raiz = Tk()
        self.__listbox = Listbox(self.raiz, width=25, height=10, border=3)
        self.__listbox.pack()

        self.frame_botoes = Frame(self.raiz)
        self.frame_botoes.pack()

        self.botao_jogar = Button(self.frame_botoes, text="Jogar", command=self.__iniciar__)
        self.botao_jogar.bind('<Return>', self.__iniciar__)
        self.botao_jogar.focus_force()
        self.botao_sair = Button(self.frame_botoes, text="Sair", command=self.__sair__)
        self.botao_sair.bind('<Return>', self.__sair__)

        self.botao_jogar.pack(side=LEFT)
        self.botao_sair.pack(side=RIGHT)
        self.__leitura__()
        self.raiz.title("Pontuações")
        self.raiz.mainloop()

    def __leitura__(self):
        for linha in getter():
            self.__listbox.insert(END, linha)

    def __iniciar__(self, event=None):
        self.resposta = True
        self.raiz.destroy()

    def __sair__(self, event=None):
        self.resposta = False
        self.raiz.destroy()

