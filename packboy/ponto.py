from tkinter import *
from random import randint
from time import time


class Ponto(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.tag = str(time())
        self.posicao_ponto = [randint(0, 240), randint(0, 290)]
        self.__adiciona_ponto__()

    def __adiciona_ponto__(self):
        self.posicao_ponto = [randint(0, 240), randint(0, 290)]
        self.canvas.create_oval(self.posicao_ponto[0], self.posicao_ponto[1],
                                self.posicao_ponto[0] + 5, self.posicao_ponto[1] + 5, tag=self.tag, fill="#fdf201")

    def colisao(self, coords):
        if coords["x1"] <= self.posicao_ponto[0] <= coords["x2"] and \
           coords["y1"] <= self.posicao_ponto[1] <= coords["y2"]:
            self.canvas.delete(self.tag)
            return True
        return False

    def __destroy__(self):
        self.canvas.delete(self.tag)
        self.__adiciona_ponto__()
