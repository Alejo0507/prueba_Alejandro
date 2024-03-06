import modulos.informacion as im
list_users=[]
def menu():
    
    
        op=0
        while op!=3:

            titulo="""
                _______________________
                _  Ingresar Usuarios  _
            """
            menu="""
                1.ingresar usuarios
                2.imprimir usuarios registrados
                3.salir
                """

            print(titulo,menu)
            op=int(input("elija una opcion\n>>"))

            if op==1:
               im.add_user(list_users)
            elif op==2:
               im.print_users(list_users)
            elif op==3:
                pass
                
        