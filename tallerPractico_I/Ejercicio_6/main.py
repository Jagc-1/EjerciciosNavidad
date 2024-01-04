import os
import menu as menu
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
            menu.registrar_dependencia()
        elif opMenu == 2:
            menu.registrar_consumo()
        elif opMenu == 3:
            menu.ver_co2_producido()
        elif opMenu == 4:
            menu.dependencia_mayor_co2()
        elif opMenu == 5:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            x = input("Press any Key...")
