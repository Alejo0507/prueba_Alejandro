
import modulos.corefile as co
inventario={
   

}

def menu():
       
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
               co.add_productos(inventario)
            elif op==2:
               pass
            
        