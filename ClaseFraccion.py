import re
class Fraccion:
    __numerador=0
    __denominador=0
    
    def __init__(self,num1,num2):
        self.__numerador=num1
        self.__denominador=num2

    def __mul__ (self,otrafraccion):
        return str(int(self.__numerador)*int(otrafraccion.__numerador))+"/"+str(int(self.__denominador)*int(otrafraccion.__denominador))

    def __add__(self,otrafraccion):
        return str(int(self.__numerador)*int(otrafraccion.__denominador)+int(self.__denominador)*int(otrafraccion.__numerador))+"/"+str(int(self.__denominador)*int(otrafraccion.__denominador))
    
    def __floordiv__(self,otrafraccion):
        return str(int(self.__numerador)*int(otrafraccion.__denominador))+"/"+str(int(self.__denominador)*int(otrafraccion.__numerador))

    def __sub__(self,otrafraccion):
        return str(int(self.__numerador)*int(otrafraccion.__denominador)-int(self.__denominador)*int(otrafraccion.__numerador))+"/"+str(int(self.__denominador)*int(otrafraccion.__denominador))

    def simplificar(self,fraccion):
        num=re.findall('[-0-9]+',fraccion)
        n1=int(num[0])
        n2=int(num[1])
        i=2
        while i<9:
            if n1%i==0 and n2%i==0:
                n1//=i
                n2//=i
            else:
                i+=1

        if n2 ==1:
            return str(n1)
        else:
            return str(n1)+'/'+str(n2)

