import tkinter as tk
from tkinter import ttk

from ProvinciaForm import ProvinciaForm

class nuevoprovincia(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.form=ProvinciaForm(self, False)
        self.btnconfirm= ttk.Button(self, text="Confirmar", command=self.confirm)
        self.paciente=None
        self.form.place(anchor=tk.N, relwidth=0.9, relheight=0.9, relx=0.5)
        self.btnconfirm.place(anchor=tk.S, relwidth=0.35, relheight=0.15, relx= 0.5, rely=0.9)

    def confirm(self):
        self.paciente=self.form.CrearProvincia()
        if self.paciente:
            self.destroy()



    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente