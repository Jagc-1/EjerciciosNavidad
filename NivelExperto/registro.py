import os
campers = []
training_routes = {
    'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)': [],
    'Programación Web (HTML, CSS y Bootstrap)': [],
    'Programación formal (Java, JavaScript, C#)' : [],
    'Bases de datos (Mysql, MongoDb y Postgresql).': [],
    'Backend (NetCore, Spring Boot, NodeJS y Express)': []
}

trainers = {
        'trainer_A': [
            'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)',
            'Programación Web (HTML, CSS y Bootstrap)'
        ],
        'trainer_B': [
            'Programación Web (HTML, CSS y Bootstrap)',
            'Programación formal (Java, JavaScript, C#)',
        ],
        'trainer_C': [
            'Bases de datos (Mysql, MongoDb y Postgresql).',
            'Backend (NetCore, Spring Boot, NodeJS y Express)'
        ]
    }

#function add_camper is for register each camper
def add_camper():
    id_number = input("Ingrese el número de identificación: ")
    name = input("Ingrese los  nombres: ")
    last_name = input("Ingrese los apellidos: ")
    adress = input("Ingrese la dirección: ")
    attendant = input("Ingrese el nombre del acudiente: ")
    mobile_phone_number =  input("Ingrese el número de telefono celular: ")
    phone_number = input("Ingrese el número de telefono fijo(Si no tiene telefono fijo coloca el numero celular): ")
    estado = input("Ingrese el estado del camper: ").lower()
    node = None
    java = None
    netcore = None

    camper_info = {
        'id_number': id_number,
        'name': name,
        'last_name': last_name,
        'adress': adress,
        'attendant': attendant,
        'phone_number': phone_number,
        'mobile_phone_number': mobile_phone_number,
        'estado': estado,
        'notas':{
            'Nota_practica': 0,
            'Nota_teorica': 0
        },
        'rutas':{
            'Node Js': node,
            'Java': java,
            'NetCore': netcore
        },
        'info_matricula':{
            'experto encargado': None,
            'ruta de entrenamiento asignada': None,
            'fecha de inicio': None,
            'fecha finalizacion': None,
            'salón de entrenamiento': None,
            'ruta_entrenamiento': None,
            'horario': None
        }
    }
    campers.append(camper_info)
    print(trainers)
    return campers

def get_camper():
    id_number = input("Ingrese el número de identificación: ")

    for camper in campers:
        if camper['id_number'] == id_number and camper['estado'] == 'inscrito':
            print("Esta identificación está en el sistema.")

            new_practice_note = float(input("Ingrese el puntaje de la nota práctica: "))
            new_theoretical_note = float(input("Ingrese el puntaje de la nota teórica: "))

            camper['notas']['Nota_practica'] = new_practice_note
            camper['notas']['Nota_teorica'] = new_theoretical_note
            print("Notas ingresadas correctamente.")

            sum_total_notes = new_practice_note + new_theoretical_note
            average_note = sum_total_notes // 2

            print(f"Promedio de notas: {average_note}")

            if average_note > 60:
                camper['estado'] = 'aprobado'
            else:
                camper['estado'] ='rechazado'

            print('El camper ha sido: ',camper['estado'])
            os.system('pause')
            break
    else:
        print("No se encontró un camper con la identificación y estado especificados.")
