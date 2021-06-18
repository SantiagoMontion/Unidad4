import tkinter as tk
from tkinter import ttk


from ListaProvincia import ListaProvincia
from UpdateProvincia import UpdateProvincia


class ProvinciasView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista Provincia")
        self.geometry("500x350")
        self.config(padx=15, pady=20)
        self.list= ListaProvincia(self)
        self.provincia=UpdateProvincia(self)
        self.agregarbtn= ttk.Button(self, text="Agregar Provincia")
        
        self.list.place(anchor=tk.SW, rely=1, relwidth=0.3, relheight=1)
        self.provincia.place(anchor=tk.NE, rely=0, relx=0.95, relwidth=0.6, relheight=0.8)
        self.agregarbtn.place(anchor= tk.CENTER, rely= 0.9, relx = 0.65, relwidth= 0.3, relheight=0.1)

    def setControlador(self, ctrl):
        self.agregarbtn.config(command=ctrl.NuevoProvincia)
        self.list.doble_click(ctrl.seleccionar)

    def agregar(self, provincia):
        self.list.insertar(provincia)
    
    def verprovincia(self, provincia, tiempo):
        self.provincia.MostrarProvincia(provincia, tiempo)
    def obtenerdetalles(self):
        return self.provincia.CrearProvincia()
