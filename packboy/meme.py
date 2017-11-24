from tkinter import *
from threading import _start_new_thread


class Meme(object):
    def __init__(self, canvas, pele='yelow', olhos="blue", maxX=250, maxY=300, coords=None, tag="padrao"):
        self.tela = canvas
        self.tag = tag
        self.placar = 0
        self.maxX, self.maxY = maxX, maxY
        self.coords = {"x1": 90, "y1": 90, "x2": 110, "y2": 110} if coords is None else coords
        self.tela.create_oval(self.coords["x1"], self.coords["y1"], self.coords["x2"], self.coords["y2"],
                              tag=self.tag, fill=pele)

        self.tela.create_oval(self.coords["x1"] + 3, self.coords["y1"] + 10,
                              self.coords["x2"] - 12, self.coords["y2"] - 15, tag=self.tag, fill=olhos)

        self.tela.create_oval(self.coords["x1"] + 12, self.coords["y1"] + 10,
                              self.coords["x2"] - 3, self.coords["y2"] - 15, tag=self.tag, fill=olhos)

        self.tela.create_arc(self.coords["x1"] + 2, self.coords["y1"] - 3,
                             self.coords["x2"] - 2, self.coords["y2"] - 3, tag=self.tag, start=220, extent=100, style=ARC)

    def esquerda(self, event):
        if self.coords["x1"] > 0:
            self.tela.move(self.tag, -10, 0)
            self.coords["x1"] -= 10
            self.coords["x2"] -= 10
        else:
            self.tela.move(self.tag, 10, 0)
            self.coords["x1"] += 10
            self.coords["x2"] += 10
            # self.mostra_coors()

    def direita(self, event):
        if self.coords["x2"] < self.maxX:
            self.tela.move(self.tag, 10, 0)
            self.coords["x1"] += 10
            self.coords["x2"] += 10
        else:
            self.tela.move(self.tag, -10, 0)
            self.coords["x1"] -= 10
            self.coords["x2"] -= 10
            # self.mostra_coors()

    def cima(self, event):
        if self.coords["y1"] > 0:
            self.tela.move(self.tag, 0, -10)
            self.coords["y1"] -= 10
            self.coords["y2"] -= 10
        else:
            self.tela.move(self.tag, 0, 10)
            self.coords["y1"] += 10
            self.coords["y2"] += 10
            # self.mostra_coors()

    def baixo(self, event):
        if self.coords["y2"] < self.maxY:
            self.tela.move(self.tag, 0, 10)
            self.coords["y1"] += 10
            self.coords["y2"] += 10
        else:
            self.tela.move(self.tag, 0, -10)
            self.coords["y1"] -= 10
            self.coords["y2"] -= 10
            # self.mostra_coors()

    def mostra_coors(self):
        print("x = {0}, {2} y = {1}, {3}".format(self.coords["x1"], self.coords["y1"],
                                                 self.coords["x2"], self.coords["y2"]))
