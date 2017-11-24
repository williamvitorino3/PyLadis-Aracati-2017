from tkinter import *
from random import randint
from meme import Meme
from threading import _start_new_thread as thread
from time import sleep


class Game(object):
    def __init__(self, raiz):
        self.tela = raiz
        self.canvas = Canvas(self.tela, height=300, width=250, takefocus=1, bg='#ffffff', highlightthickness=0)
        self.menino = Meme(canvas=self.canvas, pele="#fef707", olhos="blue",
                           coords={"x1": 120, "y1": 90, "x2": 140, "y2": 110})

        self.menina = Meme(canvas=self.canvas, pele="#f564e6", olhos="deepskyblue",
                           coords={"x1": 90, "y1": 90, "x2": 110, "y2": 110}, tag="pl2")

        self.canvas.bind('<Left>', self.menino.esquerda)
        self.canvas.bind('<Right>', self.menino.direita)
        self.canvas.bind('<Up>', self.menino.cima)
        self.canvas.bind('<Down>', self.menino.baixo)

        self.canvas.bind('<a>', self.menina.esquerda)
        self.canvas.bind('<d>', self.menina.direita)
        self.canvas.bind('<w>', self.menina.cima)
        self.canvas.bind('<s>', self.menina.baixo)


        self.canvas.focus_force()

        self.posicao_ponto = [randint(0, 240), randint(0, 290)]

        self.label_placar = Label(raiz, text=self.placar(self.menino.placar, self.menina.placar))
        # self.label_pontos = Label(raiz, text="x = {0}, y = {1}".format(self.posicao_ponto[0], self.posicao_ponto[1]))
        self.label_placar.pack()
        # self.label_pontos.pack()
        self.canvas.pack()

        thread(self.colisao, ())

        self.canvas.create_oval(self.posicao_ponto[0], self.posicao_ponto[1],
                                self.posicao_ponto[0] + 5, self.posicao_ponto[1] + 5, tag=".", fill="#000000")

        thread(self.tempo, ())
        # thread(self.__mostrar_posicao, ())
        # thread(self.movimento_bolinha, ())

    @staticmethod
    def placar(placar1, placar2):
        return "Player 1: {0}\nPlayer 2: {1}".format(placar1, placar2)

    def movimento_bolinha(self):
        from time import sleep
        while True:
            sleep(0.01)
            self.canvas.move(".", randint(-2, 2), randint(-2, 2))

    def colisao(self, colidiu=False):
        while True:
            if self.menino.coords["x1"] <= self.posicao_ponto[0] <= self.menino.coords["x2"] and \
               self.menino.coords["y1"] <= self.posicao_ponto[1] <= self.menino.coords["y2"]:
                    self.menino.placar += 1
                    colidiu = True
            if self.menina.coords["x1"] <= self.posicao_ponto[0] <= self.menina.coords["x2"] and \
               self.menina.coords["y1"] <= self.posicao_ponto[1] <= self.menina.coords["y2"]:
                    self.menina.placar += 1
                    colidiu = True

            if colidiu:
                colidiu = False
                self.label_placar["text"] = self.placar(self.menino.placar, self.menina.placar)
                self.posicao_ponto = [randint(0, 250), randint(0, 300)]
                self.canvas.delete(".")
                # self.label_pontos["text"] = "x = {0}, y = {1}".format(self.posicao_ponto[0], self.posicao_ponto[1])
                self.canvas.create_oval(self.posicao_ponto[0], self.posicao_ponto[1],
                                        self.posicao_ponto[0]+5, self.posicao_ponto[1]+5, tag=".", fill="#000000")

    def __mostrar_posicao(self):
        geometria = self.tela.winfo_geometry()
        while True:
            atual = self.tela.winfo_geometry()
            if atual != geometria:
                geometria = atual
                print(geometria)

    def tempo(self, segundos=60):
        self.parar = False
        for segundo in range(segundos, 0, -1):
            if not self.parar:
                print("Restantes: {0} : {1}".format(int(segundo/60), int(segundo%60)))
                sleep(1)
            else:
                break
        self.tela.quit()


instancia = Tk()
instancia.title("Pack's War")
instancia.geometry("250x332+550+263")
instancia.resizable(False, False)
jogo = Game(instancia)
instancia.mainloop()
jogo.parar = True
