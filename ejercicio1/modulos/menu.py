import os

import modulos.convertidor as cv
def menu():
    
    
        op=0
        while op!=5:

            titulo="""
                _______________________
                _  convertir moneda   _
            """
            menu="""
                1.convertir pesos a dolar
                2.convertir pesos a euros
                3.convertir euros a pesos
                4.convertir pesos a yenes
                5.salir
                """

            print(titulo,menu)
            op=int(input("elija una opcion\n>>"))

            if op==1:
                cv.pesos_dolares()
            elif op==2:
                cv.pesos_euros()
            elif op==3:
                cv.euros_pesos()
            elif op==4:
                cv.pesos_yenes()
    
       
