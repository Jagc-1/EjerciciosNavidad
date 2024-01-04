import os
campers = []
training_routes = {
    'Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)': [],
    'Programación Web (HTML, CSS y Bootstrap)': [],
    'Programación formal (Java, JavaScript, C#)' : [],
    'Bases de datos (Mysql, MongoDb y Postgresql).': [],
    'Backend (NetCore, Spring Boot, NodeJS y Express)': []
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

#Function Registration_of_training_areas is for register campers notes
def Registration_of_training_areas(route_number):
    maxium_capacity = 32

    for camper in campers:
        route = list(training_routes.keys())[route_number]
        if len(training_routes[route]) <= maxium_capacity:
            if camper['estado'] == 'aprobado' and camper['ruta_entrenamiento']  == None:
                camper['info_matricula']['ruta_entrenamiento'] = route
                training_routes[route].append(camper['id_number'])
        else:
            print(training_routes)
            print("No se pueden agregar más campers a esta ruta.")
            break
    os.system('pause')




# 7. CampusLands cuenta con Entrenadores expertos encargados de dirigir cada una de las rutas de entrenamiento.
# es quiere decir que a cada entrenador se le podrán asignar diferentes rutas de entrenamiento teniendo en
# cuenta su horario.

# 8. Gestor de matriculas. La coordinación académica desea contar con un modulo de matriculas que le permita
# asignar los campers aprobados, experto encargado, ruta de entrenamiento asignada, fecha de inicio, fecha
# finalizacion y salón de entrenamiento.

# 9. Periódicamente los campers son evaluados para conocer las habilidades adquiridas durante el proceso de
# Entrenamiento, cuando finaliza cada modulo los campers deben presentar una prueba teórica y una prueba
# Practica. Esta prueba es considerada como aprobada si el promedio de las dos dan un valor >=60.

# La prueba teórica tiene un peso de 30%, la prueba practica tiene un peso del 60%. Durante el proceso el
# Entrenador realiza quices, trabajos los cuales tienen un peso del 10%. Al finalizar el proceso de evaluación
# Se considera aprobado el modulo si la nota final es > 60.
# 10. Estudiantes en riesgo. La coordinación académica cuando finaliza cada uno de los módulos de las rutas
# evalúa el rendimiento de cada uno de los campers teniendo en cuenta la nota obtenida en cada modulo. Si la nota
# Es <60 el camper queda en rendimiento bajo lo cual genera un llamado de atención por tal motivo
# Se debe permitir consultar los campers en riesgo bajo.

# 11. Modulo de reportes.
# a. Listar los campers que se encuentren en estado de inscrito.
# b. Listar los campers que aprobaron el examen inicial.
# c. Listar los entrenadores que se encuentran trabajando con campuslands.
# d. Listar los estudiantes que cuentan con bajo rendimiento.
# e. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.
# f. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta
# la ruta de entrenamiento y el entrenador encargado.
