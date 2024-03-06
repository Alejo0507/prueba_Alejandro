import os


def pesos_dolares():
    value=int(input("ingrese el valor de pesos a convertir\n>>"))

    dolares=(value/3944)

    print(f'PESOS:{value}$ - DOLARES:{dolares}$')
    

def pesos_euros():
    value=int(input("ingrese el valor de pesos a convertir\n>>"))

    euros=(value/4279)

    print(f'PESOS:{value}$ - EUROS:{euros}$')
    

def euros_pesos():
    value=int(input("ingrese el valor de euros a convertir\n>>"))

    pesos=(4279*value)

    print(f'EUROS:{value}$ - PESOS:{pesos}$')
       

def pesos_yenes():
    value=int(input("ingrese el valor de pesos a convertir\n>>"))

    yenes=(value/26.30)

    print(f'PESOS:{value}$ - YENES:{yenes}$')
    

    
