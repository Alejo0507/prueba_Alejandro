import json



def update_json(inventario:str ,data):
  with open("ejercicio4/data/compañia.json", "w+") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


def add_empleado(data):
 
    name = input('ingrese el nombre del empleado:\n>>')
    id = int(input(f'ingrese el ID de {name}:\n>>'))
    cargo = input(f'ingrese el cargo de {name}:\n>>')
    dias_tra = int(input(f'ingrese los dias trabajados por {name}:\n>>'))
    horas= int(input(f'ingrese las horas trabajadas por {name}:\n>>'))
    valor_dia= int(input(f'ingrese el valor del dia de {name}:\n>>'))
    descuentos= int(input(f'ingrese los descuentos de cafeteria de {name}:\n>>'))
    prestamo= int(input(f'ingrese la cuota de prestamo de {name}:\n>>'))

    empleado = {
      'id': id,
      'nombre': name,
      'cargo':cargo,
      'salario':{
            "dias_tra":dias_tra,
            "horas":horas,
            "valor_dia":valor_dia,
            "descuentos":descuentos,
            "prestamo":prestamo,
      }
    }

    data.update({id:empleado})
    update_json("compañia.json",data)