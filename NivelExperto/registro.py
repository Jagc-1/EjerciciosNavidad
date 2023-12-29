campers = []

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
        'rutas':{
            'Node Js': node,
            'Java': java,
            'NetCore': netcore
        }
    }
    campers.append(camper_info)
    return campers

def get_camper():
    id_number = input("Ingrese el número de identificación: ")
    for camper in campers:
        if camper['id_number'] == id_number and camper['estado'] == 'inscrito':
            print("este identificación si esta en el sistema")
        else:
            print("No se ha encontrando el camper")

