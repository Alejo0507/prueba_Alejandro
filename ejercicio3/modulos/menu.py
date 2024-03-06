
import modulos.corefile as co
data={}
inventario={}
def menu():
        co.check_json(inventario,data)
        
    
        op=0
        while op!=2:

            titulo="""
                _______________________
                _  Ingresar Productos _
            """
            menu="""
                1.ingresar Productos
                2.salir
                """

            print(titulo,menu)
            op=int(input("elija una opcion\n>>"))

            if op==1:
               co.add_productos(data)
            elif op==2:
               pass
            
        