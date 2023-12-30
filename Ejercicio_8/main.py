import os
import menu
import torneo as tn
limpiar_pantalla = lambda : os.system("cls")
opMenu = 0

while True:
    limpiar_pantalla()
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
         print("Error en el dato de ingreso")
         input("Presione Enter para continuar...")
    else:
        if opMenu == 1:
            os.system("cls")
            tn.register_player()
        elif opMenu == 2:
            tn.start_tournament()
        elif opMenu == 3:
            tn.get_winners()
        elif opMenu == 4:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            x = input("Press any Key...")
