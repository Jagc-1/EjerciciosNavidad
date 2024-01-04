import registro
import os

trainers: {
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
        ],
    }


def registration_manager():
    horario_final = ''
    id_number = int(input("Ingrese el número de identificación: "))
    salon_entrenamiento = input('Ingrese el salon asignado: ')
    training_areas = int(input('que area le desea inscribir : \n1.Fundamentos de programación\n2.Programación Web\n3.Programación formal\n4.Bases de datos\n5.Backend'))
    trainer = str(input("Escoja un trainer [A - B - C]: ")).lower()
    horario = int(input("Escoje un numero para el horario [1.mañana - 2.tarde]: ")).lower()
    fechaInicio = input("Ingrese la fecha de inicio (formato DD/MM/AAAA): ")
    fechaFin = input("Ingrese la fecha de finalización (formato DD/MM/AAAA): ")
    registration_of_training_areas(training_areas)

    if  id_number in registro.camper['id_number']:
        if registro.camper['id_number'] == id_number and registro.camper['estado'] == 'aprobado' and registro.camper['ruta_entrenamiento'] is not None:
            registro.camper['info_matricula']['experto encargado'] = trainer
            registro.camper['info_matricula']['salón de entrenamiento'] = salon_entrenamiento
            if horario == 1:
                horario_final = 'mañana'
            elif horario == 2:
                horario_final = 'tarde'
            else:
                print('solo se puede ingresar los numeros 1 para mañana y 2 para tarde')

            registro.campers['info_matricula']['horario'] = horario_final
            registro.campers['info_matricula']['fecha de inicio'] = fechaInicio
            registro.campers['info_matricula']['fecha finalizacion'] = fechaFin
            print(f'Se ha matriculado al camper con ID {id_number} en la ruta {registro.camper["info_matricula"]["ruta_entrenamiento"]}.')
            print('Información de matrícula actualizada:', registro.camper['info_matricula'])
    else:
        print('No se encontró el camper')


#Function Registration_of_training_areas is for register campers notes
def registration_of_training_areas():
    maxium_capacity = 2
    id_number = int(input("Ingrese el número de identificación: "))

    route_number = 2
    route = list(registro.training_routes.keys())[route_number]
    for camper in registro.campers:
        if len(registro.training_routes[route]) <= maxium_capacity:
            print(camper['info_matricula']['ruta_entrenamiento'])
            if camper['id_number'] == id_number and camper['estado'] == 'aprobado' and camper['info_matricula']['ruta_entrenamiento']  == None:
                registro.campers['info_matricula']['ruta_entrenamiento'] = route
                registro.training_routes[route].append(camper['id_number'])
                print(registro.campers)
                print(registration_of_training_areas)
        else:
            print(registro.training_routes)
            print("No se pueden agregar más campers a esta ruta.")
    os.system('pause')

#Function to choose at which time and which trainer to select
# def schedule():
#     for camper in registro.campers:
#         if camper['id_number'] == id_number and camper['estado'] == 'aprobado' and camper['ruta_entrenamiento'] is not None:
#             camper['training_routes']['trainer'] = trainer
#             camper['training_routes']['schedule'] = horario
#             registro.training_routes['horarios'].append(camper['id_number'])
#             print(f'Se ha programado al camper con ID {id_number} en el horario {horario} con el trainer {trainer}.')
#             print('Diccionario actualizado:', registro.campers)
#             break
#     else:
#         print('No se encontró el camper.')


# training_routes = {
#     'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)': [],
#     'Programación Web (HTML, CSS y Bootstrap)': [],
#     'Programación formal (Java, JavaScript, C#)' : [],
#     'Bases de datos (Mysql, MongoDb y Postgresql).': [],
#     'Backend (NetCore, Spring Boot, NodeJS y Express)': []
# }
