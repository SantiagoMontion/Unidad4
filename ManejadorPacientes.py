from ClasePaciente import Paciente

class Manejador:
    __lista=[]
    indice=0
    def __init__(self):
        self.__lista=[]

    def agregarpaciente(self,paciente):
        self.__lista.append(paciente)
        paciente.rowid=Manejador.indice
        Manejador.indice+=1



    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__lista]

        )
        return d

    def getLista(self):
        return self.__lista
       

    def deletePaciente(self, paciente):
        indice=int(self.obtenerIndicePaciente(paciente))
        self.__lista.pop(indice)
        


    def updatePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__lista[indice]=paciente

    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__lista):
            if self.__lista[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+=1
        return i
