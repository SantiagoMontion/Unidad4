from functools import partial
from tkinter import ttk as tk
from tkinter import *
from ClaseFraccion import Fraccion
import re
class App:
    __num=0
    __root=None
    __pantalla=None
    __index=0
    __operacion=0
    __segundonumero=0
    __operador=''
    __lista=[]
    __f1=None
    __f2=None

    def __init__(self):
        self.__root=Tk()
        self.__root.geometry("350x300")
        self.__root.title("Calculadora")
        self.__root.config(bg='#1c1c1c')
        self.__pantalla=Entry(self.__root,width=45,borderwidth=5)
        self.__pantalla.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        self.botones()
        self.__root.mainloop()

    def ponernumeros(self,num):
        self.__pantalla.insert(self.__index,num)
        self.__index+=1

    def borrarpantalla(self):
        self.__index=0
        self.__pantalla.delete(0,END)

    def borrarindividual(self):
        num=int(self.__index)-1
        self.__pantalla.delete(num)
        self.__index-=1

    def getprimer(self):
        self.__primernumero=int(self.__pantalla.get())
        self.__pantalla.delete(0,END)
        self.__index=0
        
    def conviertefraccion(self):
        listanumeros=str(self.__pantalla.get())
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        self.__pantalla.delete(0,END)
        self.__index=0
        


    def dividir(self):
        try:
            self.__operador='dividir'
            self.getprimer()
        except:
            self.__operador='dividir'
            self.conviertefraccion()
            pass

    def sumar(self):
        try:
            self.__operador='sumar'
            self.getprimer()
        except:
            self.__operador='sumar'
            self.conviertefraccion()
            pass

    def multiplicar(self):
        try:
            self.__operador='multiplicacion'
            self.getprimer()
        except:
            self.__operador='multiplicacion'
            self.conviertefraccion()
            pass
    
    def restar(self):
        try:
            self.__operador='resta'
            self.getprimer()
        except:
            self.__operador='resta'
            self.conviertefraccion()
            pass

    def operacion(self):
        num1=0
        num2=0
        num3=0
        num4=0
        listanumeros=str(self.__pantalla.get())
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        num1=self.__lista[0][0]
        num2=self.__lista[0][1]
        num3=self.__lista[1][0]
        num4=self.__lista[1][1]
        self.__f1=Fraccion(num1,num2)
        self.__f2=Fraccion(num3,num4)
        self.__lista.clear()
     
    def igual(self):
        try:
            if self.__operador=='dividir':
                try:
                    self.__segundonumero=int(self.__pantalla.get())
                    if self.__segundonumero!=0:     
                        if self.__primernumero%self.__segundonumero==0:
                            result=self.__primernumero//self.__segundonumero
                            self.__pantalla.delete(0,END)
                            self.__pantalla.insert(0,result)
                        else:
                            result=self.__primernumero/self.__segundonumero
                            self.__pantalla.delete(0,END)
                            self.__pantalla.insert(0,result)
                    else:
                        result="ERROR division por 0"
                        self.__pantalla.delete(0,END)
                        self.__pantalla.insert(0,result)
                except:
                    self.operacion()
                    r=self.__f1//self.__f2
                    print(r)
                    self.__pantalla.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__pantalla.insert(0,result)

                
            elif self.__operador=='sumar':
                try:
                    self.__segundonumero=int(self.__pantalla.get())
                    result=self.__primernumero+self.__segundonumero
                    self.__pantalla.delete(0,END)
                    self.__pantalla.insert(0,result)
                except:
                    self.operacion()
                    r=self.__f1+self.__f2
                    self.__pantalla.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__pantalla.insert(0,result)


            elif self.__operador=='multiplicacion':
                try:
                    self.__segundonumero=int(self.__pantalla.get())
                    result=self.__primernumero*self.__segundonumero
                    self.__pantalla.delete(0,END)
                    self.__pantalla.insert(0,result)
                   
                except:
                    self.operacion()
                    r=self.__f1*self.__f2
                    self.__pantalla.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__pantalla.insert(0,result)
                    
                    
            elif self.__operador=="resta":
                try:
                    self.__segundonumero=int(self.__pantalla.get())
                    result=self.__primernumero-self.__segundonumero
                    self.__pantalla.delete(0,END)
                    self.__pantalla.insert(0,result)

                except:
                    self.operacion()
                    r=self.__f1-self.__f2
                    self.__pantalla.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__pantalla.insert(0,result)


            r=str(result)
            self.__index=len(r)
            self.__primernumero=0
            self.__segundonumero=0
        except:
            pass



    def botones(self):
        borrar=tk.Button(self.__root,text="C",command=partial(self.borrarpantalla)).grid(row=2,column=0,pady=3,ipady=4)
        dividir=tk.Button(self.__root,text="%",command=partial(self.dividir)).grid(row=2,column=3,pady=3,ipady=4)
        separador=tk.Button(self.__root,text="/",command=partial(self.ponernumeros,'/')).grid(row=2,column=2,pady=3,ipady=4)
        borrar1=tk.Button(self.__root,text="<-",command=partial(self.borrarindividual)).grid(row=2,column=1,pady=3,ipady=4)

        b7=tk.Button(self.__root,text="7",command=partial(self.ponernumeros,'7'))
        b7.grid(row=3,column=0,pady=3,ipady=4)
        b8=tk.Button(self.__root,text="8",command=partial(self.ponernumeros,'8')).grid(row=3,column=1,pady=3,ipady=4)
        b9=tk.Button(self.__root,text="9",command=partial(self.ponernumeros,'9')).grid(row=3,column=2,pady=3,ipady=4)
        bx=tk.Button(self.__root,text="x",command=partial(self.multiplicar)).grid(row=3,column=3,pady=3,ipady=4)

        b4=tk.Button(self.__root,text="4",command=partial(self.ponernumeros,'4')).grid(row=4,column=0,pady=3,ipady=4)
        b5=tk.Button(self.__root,text="5",command=partial(self.ponernumeros,'5')).grid(row=4,column=1,pady=3,ipady=4)
        b6=tk.Button(self.__root,text="6",command=partial(self.ponernumeros,'6')).grid(row=4,column=2,pady=3,ipady=4)
        bmenos=tk.Button(self.__root,text="-",command=partial(self.restar)).grid(row=4,column=3,pady=3,ipady=4)

        b1=tk.Button(self.__root,text="1",command=partial(self.ponernumeros,'1')).grid(row=5,column=0,pady=3,ipady=4)
        b2=tk.Button(self.__root,text="2",command=partial(self.ponernumeros,'2')).grid(row=5,column=1,pady=3,ipady=4)
        b3=tk.Button(self.__root,text="3",command=partial(self.ponernumeros,'3')).grid(row=5,column=2,pady=3,ipady=4)
        bmas=tk.Button(self.__root,text="+",command=partial(self.sumar)).grid(row=5,column=3,pady=3,ipady=4)

        bnegativo=tk.Button(self.__root,text="neg",command=partial(self.ponernumeros,'-')).grid(row=6,column=0,pady=3,ipady=4)
        b0=tk.Button(self.__root,text="0",command=partial(self.ponernumeros,'0')).grid(row=6,column=1,pady=3,ipady=4,ipadx=40,columnspan=2)

        bigual=tk.Button(self.__root,text="=",command=partial(self.igual)).grid(row=6,column=3,pady=3,ipady=4)




if __name__=='__main__':
    app=App()