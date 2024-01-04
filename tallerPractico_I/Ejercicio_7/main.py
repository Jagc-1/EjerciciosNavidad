import os
import menu
import stock as st
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
            st.registrar_producto()
        elif opMenu == 2:
            st.visualizar_productos()
        elif opMenu == 3:
            st.actualizar_stock()
        elif opMenu == 4:
             st.informe_productos_criticos()
        elif opMenu == 5:
            st.calcular_ganancia_potencial()
        elif opMenu == 6:
            print("¡Hasta luego!. Gracias Por Visitarnos")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            x = input("Press any Key...")
