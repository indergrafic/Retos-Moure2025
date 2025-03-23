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
    consulta1: int = 0
    consulta2: int = 0
    while True:
        persona = int(input("Indique su DNI(4 primeros numeros): "))
        if persona in listado:
            print(f'Usted ya esta en lista de espera, su codigo es {listado[persona]}')
        else:
            letra_num = random.choice(cod_letras)+random.choice(cod_num)+random.choice(cod_letras)
            cod_paciente.append(letra_num)
            listado[persona] = letra_num
            print(cod_paciente)
            print(listado)

        """Estos if comprueban el estado de la sala. Si estan vacios hace pasar a un paciente.
        Al mismo tiempo se borra ese paciente de la lista"""
        try:
            if consulta1 == 0:
                elem = ""
                for i in cod_paciente[0]:
                    elem += i
                print(f"{elem}     CONSULTA1")
                consulta1 = 1
        except:
            continue
        try:    
            if consulta2 == 0:
                elem = ""
                for i in cod_paciente[1]:
                    elem += i
                print(f"{elem}   CONSULTA2")
                consulta2 = 1
        except:
            continue
            
        """Se pulsara s para saber que se ha terminado la consulta y se pasara al proximo paciente"""
        consulta1_vacia = input("Sala 1 en espera. -Pulsar s-")
        consulta2_vacia = input("Sala 2 en espera. -Pulsar s-")
        if consulta1_vacia == "s":
            consulta1 = 0
            try:
                prim_clave = next(iter(listado))
                del listado[prim_clave]
                cod_paciente.pop(0)
            except:
                continue
        elif consulta2_vacia == "s":
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