import tkinter as tk
from tkinter import ttk

from ProvinciaForm import ProvinciaForm
class UpdateProvincia(ProvinciaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, True, **kwargs)
    def limpiar(self):
        self.clean()