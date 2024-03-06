import json
import os


def check_json(archivo: str, data):
  if os.path.isfile(archivo):
    with open(archivo, "r") as file:
      return json.load(file)
  else:
    with open(archivo, "w") as file:
      json.dump(data, file, indent=2)
      return data

def update_json(archivo, data):
  with open("data/"+archivo, "w+") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)


def add_productos(data):
 
    name = input('ingrese el nombre del producto:\n>>')
    id = input(f'ingrese el ID de {name}:\n>>')
    value = input(f'ingrese el Valor unitario de {name}:\n>>')
    min = int(input(f'ingrese el stock minimo de {name}:\n>>'))
    max = int(input(f'ingrese el stock maximo de {name}:\n>>'))

    producto = {
      'id': id,
      'name': name,
      'valor':value,
      'stockmin':min,
      'stockmax': max,
    }

    data.update({id: producto})
    update_json("inventario.json",data)