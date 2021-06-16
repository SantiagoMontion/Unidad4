from ObjectEncoder import ObjectEncoder
from ManejadorPacientes import Manejador
from ClasePaciente import Paciente

class Repositorio():
    __conn=None
    __manejador=None

    def __init__(self,conn):
        self.__conn=conn
        dic=self.__conn.LeerJson()
        self.__manejador=self.__conn.decodificador(dic)

    def obtenerlista(self):
        return self.__manejador.getLista()

    def agregarpaciente(self, paciente):
        self.__manejador.agregarpaciente(paciente)
        self.grabarDatos()
        return paciente

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente


    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)

    def grabarDatos(self):
        self.__conn.GuardarArchivo(self.__manejador.toJSON())
        
