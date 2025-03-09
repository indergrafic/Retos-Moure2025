agenda = {}

def insertar():
    nombre = input("\nIndique un nombre: ")
    while True:
        movil = input("\nIndique un número de movil: ")
        if len(movil) > 11 or len(movil) <1:
            print("\nMovil incorrecto, repita número\n")
        else:
            movil = int(movil)
            print("Contacto guardado.\n")
            break
    agenda[nombre] = movil

def visualizar():
    print("Contactos en Agenda\n")
    print(f"{agenda}\n")

def eliminar():
    nombre = input("\nIndica nombre a eliminar: ")
    del agenda[nombre]

def buscar():
    nombre = input("\nIndica nombre a buscar: ")
    if nombre in agenda:
        print(f"Nombre encontrado, su movil es: {agenda[nombre]}\n")
    else:
        print("El nombre buscado no existe.")
        
def actualizar():
    nombre = input("Nomre del movil para actualizar: ")
    movil = int(input("Indique el nuevo movil: "))
    agenda[nombre] = movil

while True:
    print("AGENDA DE CONTACTOS\n\n1- Insertar.\n2- Visualizar.\n3- Eliminar.\n\
4- Busqueda\n5- Actualizar\n6- Salir.")

    opcion = input("\nElija una opción: ")

    if opcion == "1":
        insertar()
    elif opcion == "2":
        visualizar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        buscar()
    elif opcion == "5":
        actualizar()
    elif opcion == "6":
        print("\nSesión Cerrada.")
        break
    else: 
        print("Opción no existe")
