import os
import menu  # Asumo que menu es un módulo definido correctamente

registro = []
NroMuestra = 5

while True:
    os.system("cls")
    opMenu = menu.menuPrincipal()

    if opMenu == 1:
        codigo = input("Ingrese código: ")
        ciudad = input("Ingrese nombre de la ciudad: ")
        registro.append([codigo, ciudad, 0.0])
        os.system("cls")
    elif opMenu == 2:
        buscarCod = input("Ingrese el código de la ciudad: ")
        print(f"Código\t\tNombre Ciudad\t\tPromedio Sismos")
        for ciudad_item in registro:
            if buscarCod == ciudad_item[0]:
                print(f"{ciudad_item[0]}\t\t{ciudad_item[1]}\t\t\t{ciudad_item[2]}")
                suma = 0
                for _ in range(NroMuestra):
                    valor_telurico = float(input("Ingrese el valor del movimiento Telúrico: "))
                    suma += valor_telurico
                ciudad_item[2] = suma / NroMuestra
        input("Presione Enter...")
    elif opMenu == 3:
        buscarCod = input("Ingrese el código de la ciudad: ")
        encontrado = False
        for ciudad_item in registro:
            if buscarCod == ciudad_item[0]:
                print(f"{ciudad_item[0]}\t\t{ciudad_item[1]}\t\t{ciudad_item[2]}")
                encontrado = True
                break
        if not encontrado:
            print("Ciudad no encontrada.")
        input("Presione Enter...")
    elif opMenu == 4:
        menu.informe_riesgo(registro)
        input("Informe de riesgo registrado. Presione Enter...")
    elif opMenu == 5:
        print("¡Busca Refugio!....")
        break
    else:
        print("La opción ingresada no es válida")
        input("Presione Enter...")
