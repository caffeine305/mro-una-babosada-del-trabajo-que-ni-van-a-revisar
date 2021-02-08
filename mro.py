# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:22:41 2021

@author: virgilio_lazaro
"""
import pandas as pd

def main():

    coeficientes=[]
    gradoPolinomio = []

    resultado =[]
    derivada = []
    
    pruebaFB = []
    
    #Solución Inicial:
    rt = 0.1
    r_final_1 = 0.0
    
    Tabla=pd.read_excel("Archivo canonica.xlsx")
    
    datosGrado = Tabla["grado"].fillna(0).tolist()
    datosCoeficiente = Tabla["coeficiente"].fillna(0).tolist()
    grado = len(datosGrado)
    longitud = len(datosCoeficiente)
           
    for j in range(5):
        
        print("El polinomio introducido es: ")
        for i in range(grado):
            c = datosCoeficiente[i] / pow((1+rt),datosGrado[i]-1) #Meter la función que debe ser
            print(c, end="")
            resultado.append(c)
            
            if(i<grado-1):        
                print(" + ", end="")
        
        print("")
        print("")
        print("La derivada del polinomio introducido es: ")
        for i in range(1,grado):
            d = -datosCoeficiente[i] / ((datosGrado[i]-1) * pow((1+rt),datosGrado[i]) )
            derivada.append(d)
            print(d,end="")
            
            if(i<grado-1):        
                print(" + ", end="")
    
        r_final = sum(resultado)
        r_deriv = sum(derivada)

        resultado.clear()
        derivada.clear()
        
        print("")
        print("")
        print("Suma: ",r_final)
        print("")
        print("Suma Derivada: ",r_deriv)
        print("")
        
        print("")
        #Cálculo de Newton Raphson
        rt_1 = rt - (r_final/r_deriv)
        print("raiz aprox.: ")
        print(rt_1)
        rt = rt_1
        error = r_final_1 - r_final
        r_final_1 = r_final
        print("")
        print("Error: ")
        print(error)
        print("")
        

        
        
if __name__ == "__main__":
    main() #Aqui se recibe el dato de la c, r en el contrato. 

#Meter VNA y su derivada
#condición inicial 0.1
#Si ya está Newton Rapson, implementalo
#Iterar hasta error menor a 10-9"
