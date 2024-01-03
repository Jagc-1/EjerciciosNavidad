import os
import menu
import registro as rg
limpiar_pantalla = lambda : os.system("cls")
opMenu = 0
info = ''
camper = None

while True:
    limpiar_pantalla()
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
         print("Error en el dato de ingreso")
         input("Presione Enter para continuar...")
    else:
        if opMenu == 1:
            rg.add_camper()
            os.system("pause")
        elif opMenu == 3:
            rg.get_camper()
            os.system("pause")
        elif opMenu == 4:
            rg.Registration_of_training_areas()
        elif opMenu == 10:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
