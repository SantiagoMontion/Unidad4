import tkinter as tk
from tkinter import  ttk

from Provincia import Provincia

class ListaProvincia(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding="3 3 3 3", **kwargs)
        self.__lb= tk.Listbox(self, **kwargs)
        scroll= ttk.Scrollbar(self, command=self.__lb.yview)
        self.__lb.config(yscrollcommand=scroll.set)
        self.__lb.place(anchor=tk.SW, rely = 1, relx= 0, relwidth=0.9, relheight=1)
        scroll.place(anchor=tk.SE, rely = 1, relx = 1, relwidth= 0.1, relheight = 1)
        
    def insertar(self, provincia, index=tk.END):
        texto = "{}".format(provincia.getnombre())
        self.__lb.insert(index, texto)
    def doble_click(self, callback):
        handler=lambda  _: callback(self.__lb.curselection()[0])
        self.__lb.bind("<Double-Button-1>", handler)