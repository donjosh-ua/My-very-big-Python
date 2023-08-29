#Aqui se va a programar de verdad
#El que vea identando mas de 3 veces me lo cojo

import os

def manejoPersonal():
    print("")

def cartasRecetas():
    print("")

def comprasVentas():
    print("")

def publicidad():
    print("")

while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\t\t\tMENU

    <1> Manejo de personal
    <2> Cartas y recetas
    <3> Compras y ventas
    <4> Publicidad
    <5> Salir\n\n""")

    option = int(input("Su opcion: "))

    if option == 1:
        manejoPersonal()

    elif option == 2:
        cartasRecetas()

    elif option == 3:
        comprasVentas()

    elif option == 4:
        publicidad()
        
    elif option == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t\tGracias!")
        break
