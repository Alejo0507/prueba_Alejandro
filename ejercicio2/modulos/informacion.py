

def add_user(list_users):
    list_user=[]
    
    titulo="""
                _______________________
                _  registrar usuario  _


            """


    print(titulo)
    name=(input("ingrese su nombre completo:\n>>"))
    id=int(input(f'ingrese su ID {name}:\n>>'))
    last_name=(input(f'ingrese sus Apellidos {name}:\n>>'))
    direccion=(input(f'ingrese su direccion {name}:\n>>'))
    city=(input(f'ingrese su ciudad {name}:\n>>'))
    long=(input(f'ingrese su longitud (ubicacion) {name}:\n>>'))
    lati=(input(f'ingrese su latitud (ubicacion) {name}:\n>>'))
    email=(input(f'ingrese su email {name}:\n>>'))
    age=int(input(f'ingrese su edad {name}:\n>>'))
    job=(input(f'ingrese su ocupacion {name}:\n>>'))

    user={
    "name":name,
    "id":id,
    "last_name":last_name,
    "direccion":direccion,
    "city":city,
    "long":long,
    "lati":lati,
    "email":email,
    "edad":age,
    "job":job,

    }

    list_user.append(user)
    list_users.append(list_user)

def print_users(list_users):
    print(list_users)
