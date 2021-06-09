from tkinter import *
from tkinter import StringVar, ttk,messagebox

class Aplicacion:
    __ventana=None
    __altura=None
    __peso=None


    def __init__(self) -> None:
        self.__ventana=Tk()
        self.__ventana.geometry("430x400")
        self.__ventana.title("Calculadora IMC")
        self.__ventana.resizable(0,0)
        
        mainframe=ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(3, weight=1)
        ttk.Label(mainframe,text="Calculadora de IMC",font=19).grid(column=0,row=0,padx=120)

        self.__altura=StringVar()
        self.__peso=StringVar()

        ttk.Label(mainframe,text="Altura: ",font=12).grid(column=0,row=1,sticky=(W),pady=45)
        self.alturaEntry=ttk.Entry(mainframe,width=8,textvariable=self.__altura)
        self.alturaEntry.grid(column=0, row=1, sticky=(W),pady=15,padx=60,ipadx=100)
        ttk.Label(mainframe,text="cm",font=12).grid(column=0,row=1,pady=15,sticky=(E))

        ttk.Label(mainframe,text="Peso: ",font=12).grid(column=0,row=2,sticky=(W),pady=25)
        self.pesoEntry=ttk.Entry(mainframe,width=8,textvariable=self.__peso)
        self.pesoEntry.grid(column=0, row=2, sticky=(W),pady=25,padx=60,ipadx=100)
        ttk.Label(mainframe,text="kg",font=12).grid(column=0,row=2,pady=25,sticky=(E))

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'green', foreground = 'white', width = 20, borderwidth=1, focusthickness=3)
        style.map('TButton', background=[('active','#81f777')],foreground=[('active','black')])

        ttk.Button(mainframe,text="Calcular",command=lambda:self.calcularpeso(mainframe)).grid(column=0, row=3, sticky=W,pady=25,padx=50)
        
        ttk.Button(mainframe,text="Limpiar",command=lambda:self.limpiarpantalla(mainframe)).grid(column=0, row=3, sticky=E,pady=25)

        self.alturaEntry.focus()
        self.__ventana.mainloop()


    def calcularpeso(self,mainframe):
        try:
            alt=int(self.alturaEntry.get())
            peso=int(self.pesoEntry.get())
            imc=float(peso/(alt/100)**2)
            print(imc)
            if imc<18.5:
                variable="Peso inferior al normal"
            elif imc>18.5 and imc<24.9:
                variable="Normal"
       
            elif imc > 25.0 and imc <29.9:
                variable="Peso superior al normal"

            elif imc>=30.0:
                variable="Obesidad"
            self.secondframe=ttk.Frame(self.__ventana)
             
            self.secondframe.grid(column=0, row=3, sticky=(N, W, E, S))
            ttk.Label(self.secondframe,text="Tu indice de masa corporal (IMC) es {0:.2f} kg/m2".format(imc),font=8).grid(column=0,row=4,pady=10,padx=30)
            ttk.Label(self.secondframe,text=variable,font=12).grid(column=0,row=5,pady=10,padx=100)

        except:
            messagebox.showerror(title='Error de tipo',
            message='Debe ingresar un valor numérico')

    def limpiarpantalla(self,mainframe):
        self.pesoEntry.delete(0,END)
        self.alturaEntry.delete(0,END)
        for widgets in self.secondframe.winfo_children():
            widgets.destroy()


def test():
     app=Aplicacion()

if __name__=='__main__':
    test()