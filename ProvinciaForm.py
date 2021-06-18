import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Provincia import Provincia
class ProvinciaForm(ttk.Labelframe):
    
    __fields=("Nombre", "Capital", "Habitantes", "Partidos", "Temperatura", "Sensación", "Humedad")
    __allfields=bool

    def __init__(self, master, allfields,**kwargs):
        super().__init__(master, text="Provincia", **kwargs)
        self.__allfields = allfields
        if self.__allfields:
            self.entries= list(map(self.CrearCampo, enumerate(self.__fields)))
        else:
            self.entries = list(map(self.CrearCampo, enumerate(self.__fields[0:4])))

    def CrearCampo(self, field):
        position, text = field
        label= ttk.Label(self, text=text)
        label.config()
        entry = ttk.Entry(self)
        if self.__allfields:
            position = position/7
        else:
            position = position/5

        label.place(anchor=tk.NW, rely= position, relx = 0.017, relheight= 0.1, relwidth = 0.3)
        entry.place(anchor=tk.NW, rely= position, relx = 0.3, relheight= 0.1, relwidth= 0.6)
        return entry
    def MostrarProvincia(self, prov, tiempo):
        if "cod" not in tiempo:
            values=(prov.getnombre(), prov.getcapital(), prov.gethabitantes(), prov.getpartido(), tiempo["Temperatura"], tiempo["sensacion"], tiempo["humedad"])
        else:
            values=(prov.getnombre(), prov.getcapital(), prov.gethabitantes(), prov.getpartido(),"Error", "Error", "Error")
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def CrearProvincia(self):
        prov=Provincia
        values=[e.get() for e in self.entries]
        try:
            prov=Provincia(*values)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)
        else:
            return prov
    def clean(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
