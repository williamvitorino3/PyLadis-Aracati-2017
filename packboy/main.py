#!/usr/bin/env python

from singleplayer import *
from records import *
from lista_pontos import *

marca = "###### WV Desenvolvimentos ######"
propaganda = '#'*len(marca) + "\n" + marca + "\n" + '#'*len(marca)

print(propaganda)

while ListaPontos().resposta:
    try:
        instancia = Tk()

        instancia.title("PackBoy")
        instancia.geometry("260x350+550+263")
        instancia.resizable(False, False)

        jogo = Game(instancia)

        instancia.mainloop()
        instancia.destroy()

        instancia = Tk()
        instancia.title("Salvar Pontos")
        Recorde(instancia, jogo.menino.placar)
        instancia.geometry("+550+263")

        instancia.mainloop()
        instancia.destroy()
    except Exception:
        continue
