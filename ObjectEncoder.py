import json
from Provincia import Provincia
from Mprovincias import ManejaProvincia

class ObjectEncoder(object):
    def Guardar(self, elementos, archivo):
        with open(archivo, "w", encoding="UTF-8")as file:
            json.dump(elementos, file, indent=4)
        return True
    def Leer(self, archivo):
        with open(archivo, encoding="UTF-8")as file:
            aux = json.load(file)
        return aux
    def Decoder(self, d):
        if "__class__" not in d:
            return d 
        else:
            class_name = d["__class__"]
            class_=eval(class_name)
            if class_name == "ManejaProvincia":
                elements = d["Elementos"]
                Elementos = class_()
                for i in range(len(elements)):
                    delemento = elements[i]
                    class_name = delemento.pop("__class__")
                    class_ = eval(class_name)
                    atributos = delemento["__atributos__"]
                    prov = class_(**atributos)
                    Elementos.agregar(prov)
                return Elementos