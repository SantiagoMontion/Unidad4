from ClasePrecio import Precio
import requests
class Manejador:
    __lista=None
    __dolares=None
    def __init__(self):
        self.__lista=[]


    def listar(self):
        url='https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r=requests.get(url)
        self.__dolares=r.json()

    def agregarprecios(self):
        for i in range(len(self.__dolares)):
             if self.__dolares[i]['casa']['compra']!="No Cotiza" and self.__dolares[i]['casa']['venta']!=0 and (self.__dolares[i]['casa']['nombre']).count("Dolar")!=0:
                    pc = self.__dolares[i]['casa']['compra']
                    pv=self.__dolares[i]['casa']['venta']
                    p=Precio(pv,pc)
                    self.__lista.append(p)

    def retornalista(self):
        return self.__lista

    def retornadolares(self):
        return self.__dolares


