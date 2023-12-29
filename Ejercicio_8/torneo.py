def points_in_favor(player):
    return player["PA"]

def register_match(player, win, points_in_favor):
    player["PJ"] += 1
    if win:
        player["PG"] += 2
    else:
        player["PP"] += 1
    player["PA"] += points_in_favor
def register_player():
    max_players = 12
    total_players = 0

    players_by_categories = {
        "Novato": {"jugadores": [], "min_edad": 15, "max_edad": 16},
        "Intermedio": {"jugadores": [], "min_edad": 17, "max_edad": 20},
        "Avanzado": {"jugadores": [], "min_edad": 21, "max_edad": None}
    }

    for categorie, info in players_by_categories.items():
        print(f"Inscribir jugadores para la categoría {categorie}:")
        print("----------------------------------------")
        while len(info["jugadores"]) < 5 and total_players < max_players:
            name = input("Nombre del jugador (o 'fin' para terminar): ")
            print("----------------------------------------")

            if name.lower() == 'fin':
                break

            try:
                age = int(input("Edad del jugador: "))
                print("----------------------------------------")
            except ValueError:
                print("Por favor, ingrese una edad válida.")
                continue

            if info["min_edad"] <= age <= info["max_edad"]:
                player = {"nombre": name, "edad": age}
                info["jugadores"].append(player)
                total_players += 1
            else:
                print(f"Lo siento, el jugador debe tener entre {info['min_edad']} y {info['max_edad']} años para la categoría {categorie}.")
    return players_by_categories

def start_tournament(players_by_categories: dict) -> dict:
    header = """
    ***********************************
    * Bienvenidos al torneo de Tennis *
    ***********************************
    """
    print(header)
    name_player = input("Ingrese nombre del jugador: ")
    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if name_player == player["nombre"]:
                print("El jugador está registrado en la categoría:", category)
                return category
        else:
            print("No se encontró el jugador")

def get_winners(torneo: dict) -> dict:
    for categoria, infoCat in torneo.items():
        print("categoria: ",categoria)
        print("Infocat: ",infoCat)
        ganador = max(infoCat["jugadores"], key=points_in_favor)
        print(f"Ganador en la categoría {categoria}: {ganador['nombre']} con {ganador['PA']} puntos a favor.")
