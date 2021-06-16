from Vista import ContactsView, NewContact,VerImc
from ManejadorPacientes import Manejador

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerlista())
 # comandos que se ejecutan a través de la vista

    def crearPaciente(self):
        nuevoPaciente = NewContact(self.vista).show()
        if nuevoPaciente:
            Paciente = self.repo.agregarpaciente(nuevoPaciente)
            self.pacientes.append(Paciente)
            self.vista.agregarPaciente(Paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        Paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(Paciente)


    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        else:
            rowid = self.pacientes[self.seleccion].rowid
            detallesPaciente = self.vista.obtenerDetalles()
            detallesPaciente.rowid = rowid
            Paciente = self.repo.modificarPaciente(detallesPaciente)
            self.pacientes[self.seleccion] = Paciente
            self.vista.modificarPaciente(Paciente, self.seleccion)
            self.seleccion=-1


    def verIMC(self):
        if self.seleccion==-1:
            return
        else:
            detallesPaciente = self.vista.obtenerDetalles()
            IMC = VerImc(self.vista,int(detallesPaciente.getalt()),int(detallesPaciente.getpeso()))
            self.seleccion=-1

    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1


    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
            self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()




