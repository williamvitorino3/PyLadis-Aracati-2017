#!/usr/bin/env python

from tkinter import *
from random import randint
from meme import Meme
from threading import _start_new_thread as thread
from time import sleep
from ponto import Ponto


class Game(object):
    def __init__(self, raiz):
        self.tela = raiz
        self.canvas = Canvas(self.tela, height=300, width=250, takefocus=1, bg='#000000',
                             highlightthickness=0)

        self.menino = Meme(canvas=self.canvas, pele="#fef707", olhos="blue",
                           coords={"x1": 120, "y1": 90, "x2": 140, "y2": 110})

        self.canvas.bind('<Left>', self.menino.esquerda)
        self.canvas.bind('<Right>', self.menino.direita)
        self.canvas.bind('<Up>', self.menino.cima)
        self.canvas.bind('<Down>', self.menino.baixo)

        self.canvas.focus_force()

        self.label_placar = Label(raiz, text=self.placar(self.menino.placar), border=3)
        self.label_tempo = Label(raiz, text="00:00", border=3)
        self.label_placar.pack()
        self.label_tempo.pack()
        self.canvas.pack()

        self.lista_pontos = [Ponto(self.canvas)]

        thread(self.colisao, ())

        thread(self.tempo, ())

    def __adicionar__(self):
        self.lista_pontos.append(Ponto(self.canvas))

    @staticmethod
    def placar(placar1):
        return "Pontos: {0}".format(placar1)

    def colisao(self):
        while True:
            for ponto in self.lista_pontos.copy():
                if ponto.colisao(self.menino.coords):
                    self.menino.placar += 1
                    self.lista_pontos.remove(ponto)
                    self.label_placar["text"] = self.placar(self.menino.placar)
                    self.__adicionar__()

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
                self.__adicionar__()
                self.label_tempo["text"] = "Tempo: {0} : {1}".format(int(segundo / 60), int(segundo % 60))
                sleep(1)
            else:
                break
        self.tela.quit()
