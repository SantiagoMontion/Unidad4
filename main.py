
from VistaProvincia import ProvinciasView
from Controlador import Controlador
from Mprovincias import ManejaProvincia
from ObjectEncoder import ObjectEncoder
if __name__ == "__main__":
    encoder = ObjectEncoder()
    try: 
        aux=encoder.Leer("datos.json")
        aux=encoder.Decoder(aux)

    except FileNotFoundError:
        aux=ManejaProvincia()

    vista=ProvinciasView()
    control=Controlador(vista, aux)
    vista.setControlador(control)
    control.start()
    encoder.Guardar(control.salir(), "datos.json") 
    