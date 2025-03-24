import random
"""
El programa trata de emular el panel existente en los edificios de salud en el
que se nos indica cuando nos corresponde el turno, con la informacion siguiente:
    - Un conjunto de dos letas y un numero, ejm.: Y5J. Esta es la misma que el tique que tenemos.
    Este código es aleatorio e individual.
    - Y la cunsulta que nos corresponde, ejm.: Consulta 1.
"""
cod_paciente = []
listado = {}
def turno():
    cod_letras = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "y", "z"]
    cod_num = ["1", "2", "3","4", "5", "6", "7", "8", "9", "0"]
    """Bucle para comprobar si ya esta creado y si no es asi se crea."""
    consulta1 = 0
    consulta2 = 0
    while True:
        
        persona = int(input("Introduzca su DNI (4 primeros numeros) o (0 - para continuar): "))
        consulta_vacia = int(input("\nQue consulta esta vacia? -Pulsar 1/2 o 3 si estan ocupadas: "))
        
        match consulta_vacia:
            case 1:
                consulta1 = 1
            case 2:
                consulta2 = 1
            case _:
                print("No hay consultas vacias")

        if persona == 0:
            print("Sin paciente")
        elif persona in listado:
            print(f'Usted ya esta en lista de espera, su codigo es {listado[persona]}')
        else:
            letra_num = random.choice(cod_letras)+random.choice(cod_num)+random.choice(cod_letras)
            cod_paciente.append(letra_num)
            listado[persona] = letra_num

        """Estos if comprueban el estado de la sala. Si estan vacios hace pasar a un paciente.
        Al mismo tiempo se borra ese paciente de la lista"""
        if consulta1 == 1:
            if letra_num in cod_paciente:              
                print(f"{listado.get(persona)}     CONSULTA1")
            else: 
                print("xxxxx") 

        if consulta2 == 1:
            if letra_num in cod_paciente:              
                print(f"{listado.get(persona)}     CONSULTA2")
            else:
                continue

        """Se pulsara s para saber que se ha terminado la consulta y se pasara al proximo paciente"""
        #consulta2_vacia = input("Sala 2 vacia. -Pulsar s/n-")
        if consulta_vacia == 3:
            continue
        elif consulta_vacia == 1:
            consulta1 = 0
            try:
                prim_clave = next(iter(listado))
                del listado[prim_clave]
                cod_paciente.pop(0)
            except:
                continue
        elif consulta_vacia == 2:
            consulta2 = 0
            try:
                prim_clave = next(iter(listado))
                del listado[prim_clave]
                cod_paciente.pop(0)
            except:
                continue
        else:
            print("Espere su turno.")
        
        if len(cod_paciente) == 0 and consulta1 == 0 and consulta2 == 0:
            print("El tiempo de consulta ha terminado.\nGracias por su visita.")
            break
        
turno()