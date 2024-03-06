import json
import os

def update_json(inventario:str ,data):
  with open("ejercicio3/data/inventario.json", "w+") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


def add_productos(data):
 
    name = input('ingrese el nombre del producto:\n>>')
    id = input(f'ingrese el ID de {name}:\n>>')
    value = input(f'ingrese el Valor unitario de {name}:\n>>')
    min = int(input(f'ingrese el stock minimo de {name}:\n>>'))
    max = int(input(f'ingrese el stock maximo de {name}:\n>>'))

    producto = {
      'id': id,
      'nombre': name,
      'valor':value,
      'stockmin':min,
      'stockmax': max,
    }

    data.update({id: producto})
    update_json("inventario.json",data)