import os
import menu as mn
limpiar_pantalla = lambda : os.system("cls")
opMenu = 0

while True:
    limpiar_pantalla()
    opcion_menu = mn.menu_principal()

    if opcion_menu == 1:
        mn.registrar_dependencia()
    elif opcion_menu == 2:
        mn.registrar_consumo()
    elif opcion_menu == 3:
        mn.ver_co2_producido()
    elif opcion_menu == 4:
        mn.dependencia_mayor_co2()
    elif opcion_menu == 5:
        print("¡Hasta luego!. Gracias Por Visitarnos")
        break
    else:
        print("La opción ingresada no es válida.")
