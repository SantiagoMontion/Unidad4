from ClaseRepositorio import Repositorio
from Vista import ContactsView
from Controlador import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('pacientes.json')
    repo=Repositorio(conn)
    vista=ContactsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


if __name__ == "__main__":
    main()