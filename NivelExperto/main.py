import os
import menu
import registro as rg
import matriculas as mat

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
        elif opMenu == 2:
            rg.get_camper()
        elif opMenu == 3:
            # mat.registration_manager()
            mat.registration_of_training_areas()
        elif opMenu == 10:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
