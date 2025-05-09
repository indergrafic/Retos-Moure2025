# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio
'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */'''

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
