
import modulos.corefile as co
compañia={}
def menu():
    
    
        op=0
        while op!=4:

            titulo="""
                _____________________________________
                _  registro de empleados y nominas  _
            """
            menu="""
                1.ingresar empleados
                2.total pagado por concepto de nomina
                3.consultar la colilla de un empleado
                4.salir
                """

            print(titulo,menu)
            op=int(input("elija una opcion\n>>"))

            if op==1:
                 co.add_empleado(compañia)
                
            elif op==2:
                pass
            elif op==3:
                pass
            elif op==4:
                pass