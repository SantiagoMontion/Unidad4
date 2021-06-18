from tkinter import messagebox

from VistaProvincia import ProvinciasView
from Mprovincias import ManejaProvincia
from NuevoProvincia import nuevoprovincia
from weather import Tiempo

class Controlador(object):
    __vista= ProvinciasView
    __seleccion=int
    __provincia=ManejaProvincia
    __weather=Tiempo

    def __init__(self, vista, provincia):
        self.__vista = vista
        self.__provincia = provincia
        self.__seleccion=-1
        self.__weather=Tiempo()

    def NuevoProvincia(self):
        nuevo=nuevoprovincia(self.__vista).show()
        if nuevo:
            self.__provincia.agregar(nuevo)
            self.__vista.agregar(nuevo)

    def seleccionar(self, index):
        self.__seleccion = index
        provincia = self.__provincia.getprovincias()[index]
        self.__vista.verprovincia(provincia, self.__weather.obtener(provincia.getcapital()))

    def start(self):
        for p in self.__provincia.getprovincias():
            self.__vista.agregar(p)
        self.__vista.setControlador(self)
        self.__vista.mainloop()
        
    def salir(self):
        return self.__provincia.toJSON()

