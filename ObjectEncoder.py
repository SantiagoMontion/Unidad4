import json
from pathlib import Path
from ClasePaciente import Paciente
from ManejadorPacientes import Manejador
class ObjectEncoder:
    __patharchivo=None

    def __init__(self,path):
        self.__patharchivo=path

    def decodificador(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                pacientes=d['pacientes']
                manejador=class_()
                for i in range(len(pacientes)):
                    dPaciente=pacientes[i]
                    class_name=dPaciente.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPaciente['__atributos__']
                    unPaciente=class_(**atributos)
                    manejador.agregarpaciente(unPaciente)
            return manejador

    def GuardarArchivo(self,dic):
        with Path(self.__patharchivo).open("w", encoding="UTF-8") as destino:
            json.dump(dic,destino,indent=4)
            destino.close()

    def LeerJson(self):
        with Path(self.__patharchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario