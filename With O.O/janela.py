import tkinter as tk


class Janela(object):
    def __init__(self, root):
        self.rootWindow = tk.Frame(root)
        # Componentes
        self.inputFrame = tk.Frame(self.rootWindow)
        self.input = tk.Entry(self.inputFrame)
        self.button = tk.Button(
            self.inputFrame, text="Diga", command=self.dizer)
        self.paraDizer = tk.StringVar()
        self.label = tk.Label(self.rootWindow, textvariable=self.paraDizer)

        # Gerenciador de layout
        self.rootWindow.pack()
        self.inputFrame.pack()
        self.label.pack()
        self.input.pack(side="left")
        self.button.pack(side="right")

    def dizer(self):
        self.paraDizer.set(self.input.get())
