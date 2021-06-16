from ClasePaciente import Paciente
import tkinter as tk
from tkinter import Entry, StringVar, Variable, messagebox



class ContactList(tk.Frame):

	def __init__(self, master, **kwargs):
 		super().__init__(master)
 		self.lb = tk.Listbox(self, **kwargs)
 		scroll = tk.Scrollbar(self, command=self.lb.yview)
 		self.lb.config(yscrollcommand=scroll.set)
 		scroll.pack(side=tk.RIGHT, fill=tk.Y)
 		self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

	def borrar(self, index):
		self.lb.delete(index, index)

	def modificar(self, contact, index):
		self.borrar(index)
		self.insertar(contact, index)


	def bind_doble_click(self, callback):
		handler = lambda _: callback(self.lb.curselection()[0])
		self.lb.bind("<Double-Button-1>", handler)

	def insertar(self,paciente,index=tk.END):
		text="{},{}".format(paciente.getap(), paciente.getnom())
		self.lb.insert(index,text)
	


class ContactForm(tk.LabelFrame):
	fields = ("Apellido", "Nombre", "Teléfono","Altura","Peso")

	def __init__(self, master, **kwargs):
		super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
		self.frame = tk.Frame(self)
		self.entries=list(map(self.crearCampo,enumerate(self.fields)))
		self.frame.pack()
		
	def crearCampo(self, field):
 		position, text = field
 		label = tk.Label(self.frame, text=text)
 		entry = tk.Entry(self.frame, width=25)
 		label.grid(row=position, column=0, pady=5)
 		entry.grid(row=position, column=1, pady=5)
 		return entry
		 
	def mostrarEstadoPacienteEnFormulario(self, Paciente):
 # a partir de un paciente, obtiene el estado
 # y establece en los valores en el formulario de entrada
 		values = (Paciente.getap(), Paciente.getnom(),Paciente.gettel(),Paciente.getalt(),Paciente.getpeso())
 		for entry, value in zip(self.entries, values):
 			entry.delete(0, tk.END)
 			entry.insert(0, value)
			 
	def crearPacienteDesdeFormulario(self):
 #obtiene los valores de los campos del formulario
 #para crear un nuevo paciente
 		values = [e.get() for e in self.entries]
 		paciente=None
 		try:
 			paciente = Paciente(*values)
 		except ValueError as e:
 			messagebox.showerror("Error de Validación", str(e), parent=self)
 		return paciente
 


	def limpiar(self):
 		for entry in self.entries:
 			entry.delete(0, tk.END)




class NewContact(tk.Toplevel):

	def __init__(self, parent):
		super().__init__(parent)
		self.paciente = None
		self.title("Nuevo Paciente")
		self.form = ContactForm(self)
		self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
		self.form.pack(padx=10, pady=10)
		self.btn_add.pack(pady=10)
		self.resizable(0,0)

	def confirmar(self):
		self.paciente = self.form.crearPacienteeDesdeFormulario()
		if self.paciente:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.paciente





class VerImc(tk.Toplevel):
	def __init__(self, parent,altura,peso):
		super().__init__(parent)
		self.mainframe=tk.Frame(self)
		self.mainframe.pack(ipadx=60,ipady=40)
		self.title("IMC")
		self.paciente=None
		
		tk.Label(self.mainframe,text="IMC").pack(padx=5,pady=5,side=tk.LEFT,anchor=tk.N)
		
		self.calcular(altura,peso)

		self.btn_add = tk.Button(self, text="Volver", command=self.cerrar)
		self.btn_add.pack(pady=5)
		self.resizable(0,0)

	def calcular(self,altura,peso):	
		imc=float(peso/(altura/100)**2)

		if imc<18.5:
			variable="Peso inferior al normal"

		elif imc>18.5 and imc<24.9:
			variable="Normal"

		elif imc > 25.0 and imc <29.9:
			variable="Peso superior al normal"

		elif imc>=30.0:
			variable="Obesidad"
        

		tk.Label(self.mainframe,text="{0:.2f}".format(imc)).pack(padx=5,pady=5)
		tk.Label(self.mainframe,text="Composicion corporal {}".format(variable)).pack(pady=30)
				
		


	def cerrar(self):
		try:
			self.Entry.delete(0,tk.END)
			self.destroy()
		except:

			self.destroy()


	def show(self):
		self.grab_set()
		self.wait_window()
		return self.paciente


	






class UpdateContactForm(ContactForm):

	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
		self.btn_save = tk.Button(self, text="Guardar")
		self.btn_delete = tk.Button(self, text="Borrar")
		self.btn_imc= tk.Button(self,text="Ver IMC")
		self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
		self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
		self.btn_imc.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
		

	def bind_save(self, callback):
		self.btn_save.config(command=callback)

	def bind_delete(self, callback):
		self.btn_delete.config(command=callback)

	def bind_imc(self, callback,ctrl):
		self.btn_imc.config(command=ctrl.verIMC)




class ContactsView(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Lista de Pacientes")
		self.list = ContactList(self, height=15)
		self.form = UpdateContactForm(self)
		self.btn_new = tk.Button(self, text="Agregar paciente")
		self.list.pack(side=tk.LEFT, padx=10, pady=10)
		self.form.pack(padx=10, pady=10)
		self.btn_new.pack(side=tk.BOTTOM, pady=5)
		self.resizable(0,0)


	def setControlador(self, ctrl):
 #vincula la vista con el controlador
		self.btn_new.config(command=ctrl.crearPaciente)
		self.list.bind_doble_click(ctrl.seleccionarPaciente)
		self.form.bind_save(ctrl.modificarPaciente)
		self.form.bind_delete(ctrl.borrarPaciente)
		self.form.bind_imc(ctrl.verIMC,ctrl)
		


	def agregarPaciente(self,paciente):
		self.list.insertar(paciente)

	def modificarPaciente(self, paciente, index):
		self.list.modificar(paciente, index)


	def borrarPaciente(self, index):
		self.form.limpiar()
		self.list.borrar(index)
#obtiene los valores del formulario y crea un nuevo paciente

	def obtenerDetalles(self):
		return self.form.crearPacienteDesdeFormulario()
 #Ver estado de Paciente en formulario de Pacientes

	def verPacienteEnForm(self, paciente):
		self.form.mostrarEstadoPacienteEnFormulario(paciente)




