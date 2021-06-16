import re
class Paciente:
    emailRegex = re.compile(r"[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}")
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __nombre=''
    __apellido=''
    __telefono=''
    __altura=0
    __peso=0



    def __init__(self,apellido,nombre,telefono,altura,peso):
        self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__apellido=self.requerido(apellido, 'Apellido es un valor requerido')
        self.__telefono=self.formatoValido(telefono, Paciente.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura=self.requerido(altura,"Altura es un valor requerido")
        self.__peso=self.requerido(peso,"Peso es un valor requerido")

    def getnom(self):
        return self.__nombre

    def getap(self):
        return self.__apellido

    def gettel(self):
        return self.__telefono

    def getalt(self):
        return self.__altura

    def getpeso(self):
        return self.__peso



    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self, valor, regex, mensaje):
        if not valor and not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        nombre=self.__nombre,
                        apellido=self.__apellido,
                        telefono=self.__telefono,
                        altura=self.__altura,
                        peso=self.__peso
                )
            )
        return d

