
class Precio:
    __preciocompra=0
    __precioventa=0

    def __init__(self,pv,pc):
        self.__preciocompra=pc
        self.__precioventa=pv
    def getpc(self):
        return self.__preciocompra
    def getpv(self):
        return self.__precioventa