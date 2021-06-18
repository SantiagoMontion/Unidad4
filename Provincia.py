
class Provincia(object):
    __nombre=str
    __capital=str
    __habitantes=int
    __partidos=int

    def __init__(self, nombre, capital, hab, part):
        self.__nombre = nombre if nombre != "" else self.error("Ingrese Nombre")    
        self.__capital = capital if capital !="" else self.error("Ingrese Capital")
        self.__habitantes = hab if hab != "" else self.error("Ingrese Cantidad de Habitantes")
        self.__partidos = part if part != "" else self.error("Ingrese cantidad de partidos")

    def getnombre(self):
        return self.__nombre
    def getcapital(self):
        return self.__capital
    def gethabitantes(self):
        return self.__habitantes
    def getpartido(self):
        return self.__partidos
    def error(self, msg):
        raise ValueError(msg)
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,  
            __atributos__=dict(
                nombre = self.__nombre, 
                capital = self.__capital,
                hab = self.__habitantes,
                part = self.__partidos
            )
        )
        return d