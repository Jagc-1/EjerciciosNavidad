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
            limpiar_pantalla()
            participants = tn.register_player()
        elif opMenu ==2:
            tn.registrer_points(participants)
        elif opMenu == 3:
            tn.view_statistics(participants)
        elif opMenu == 4:
            tn.get_winners(participants)
        elif opMenu == 5:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            x = input("Press any Key...")
