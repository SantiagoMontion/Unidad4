from tkinter import *
from tkinter import ttk
import datetime
from Manejador import Manejador
class App:
    __root=None
    __hora=None

    def muestra(self,m):
        
        fila=1
        mlista=m.retornalista()
        dolares=m.retornadolares()

        

        ttk.Label(self.mainframe,text="Moneda",foreground="white",background="green",font=14).grid(row=0,column=0,sticky=(W),padx=15)
        ttk.Label(self.mainframe,text="Compra",foreground="white",background="green",font=14).grid(row=0,column=1,sticky=(W),padx=15)
        ttk.Label(self.mainframe,text="Venta",foreground="white",background="green",font=14).grid(row=0,column=2,sticky=(W),padx=25)
        for i in range(len(dolares)):
            if dolares[i]['casa']['compra']!="No Cotiza" and dolares[i]['casa']['venta']!=0 and (dolares[i]['casa']['nombre']).count("Dolar")!=0:

                Label(self.__root,text="{}".format(dolares[i]['casa']['nombre']),font=("Arial",11)).grid(row=fila,column=0,pady=20,padx=15)
                Label(self.__root,text="{}".format(dolares[i]['casa']['compra']),font=("Arial",11)).grid(row=fila,column=1,pady=20,padx=15)
                Label(self.__root,text="{}".format(dolares[i]['casa']['venta']),font=("Arial",11)).grid(row=fila,column=2,pady=20,padx=15)
                fila+=1

        fila=1


    def actualizar(self):
        self.L.destroy()
        fecha=datetime.datetime.today()
        a=fecha.year
        m=fecha.month
        d=fecha.day
        h=fecha.hour
        min=str(fecha.minute)
        self.secondframe=ttk.Frame(self.__root,padding="3 3 12 12").grid(sticky="s")
        if len(min)==1:
            min="0"+min

        self.L=ttk.Label(self.secondframe,text="Actualizado {}/{}/{} {}:{}".format(d,m,a,h,min),font=("Arial",11))
        self.L.grid(sticky="se",column=0)
        


    def __init__(self):
        m=Manejador()
        m.listar()
        m.agregarprecios()
        self.__root=Tk()
        self.L=ttk.Label(self.__root)
        self.mainframe=ttk.Frame(self.__root,padding="3 3 12 12").grid(ipadx=200,ipady=20,columnspan=3)
        style=ttk.Style()
        style.configure('TFrame', background='#6fc979')

        self.muestra(m)
        self.__root.geometry("500x500")
        self.__root.title("Cotizacion divisas")
        Button(self.__root,text="Actualizar",font=("Arial",11),command=lambda:[m.listar(),self.muestra(m),self.actualizar()]).grid(sticky='s',column=0)
        self.__root.mainloop()


if __name__=='__main__':
    app=App()
    