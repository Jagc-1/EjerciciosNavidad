def puntosFavor(jugador):
    return jugador["PA"]

def registrar_partido(jugador, ganado, puntos_a_favor):
    jugador["PJ"] += 1
    if ganado:
        jugador["PG"] += 2
    else:
        jugador["PP"] += 1
    jugador["PA"] += puntos_a_favor

def iniciar_torneo():
    max_jugadores_torneo = 12 
    total_jugadores = 0

    torneo = {
        "Novato": {"jugadores": [], "min_edad": 15, "max_edad": 16},
        "Intermedio": {"jugadores": [], "min_edad": 17, "max_edad": 20},
        "Avanzado": {"jugadores": [], "min_edad": 21, "max_edad": None}
    }

    for categoria, infoCat in torneo.items():
        print(f"Inscribir jugadores para la categoría {categoria}:")

        while len(infoCat["jugadores"]) < 5 and total_jugadores < max_jugadores_torneo:
            nombre = input("Nombre del jugador (o 'fin' para terminar): ")

            if nombre.lower() == 'fin':
                break

            edad = int(input("Edad del jugador: "))
            jugador = {"nombre": nombre, "edad": edad, "PJ": 0, "PG": 0, "PP": 0, "PA": 0}
            infoCat["jugadores"].append(jugador)
            total_jugadores += 1

def mostrar_ganadores(torneo):
    for categoria, info_categoria in torneo.items():
        ganador = max(info_categoria["jugadores"], key=puntosFavor)
        print(f"Ganador en la categoría {categoria}: {ganador['nombre']} con {ganador['PA']} puntos a favor.")
