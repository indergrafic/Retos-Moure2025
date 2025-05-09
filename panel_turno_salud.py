"""
El programa trata de emular el panel existente en los edificios de salud en el
que se nos indica cuando nos corresponde el turno, con la informacion siguiente:
- Un conjunto de dos letas y un numero, ejm.: Y5J. Esta es la misma que el tique que tenemos.
Este código es aleatorio e individual.
- Y la cunsulta que nos corresponde, ejm.: Consulta 1.
"""
import random

listado = {}

consulta1 = True
consulta2 = True
def admin_paciente():
    '''Se crea al azar el codigo individual de letra-numero-letra
    de cada paciente y se introduce en el diccionario.'''
    cod_letras = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "y", "z"]
    cod_num = ["1", "2", "3","4", "5", "6", "7", "8", "9", "0"]

    letra_num = random.choice(cod_letras)+random.choice(cod_num)+random.choice(cod_letras)
    listado[persona] = letra_num

def elim_paciente():
    '''Eliminamos al paciente  una vez ha pasado a consulta.'''
    prim_clave = next(iter(listado))
    del listado[prim_clave]
    
while True:
    persona = input("Introduzca su DNI (4 primeros numeros) o (n - para continuar): ")
    try:
        if persona == "n":
            #Acceso a la key del primer elemento del diccionario.
            persona = list(listado.keys())[0]
        else:
            admin_paciente()
    except:
        pass
    #print(f'---{listado}')
    
    try:
        if consulta1:
            print(f"{listado[persona]}     CONSULTA1")
            elim_paciente()
            consulta1 = False
    except:
        pass
    try:
        if consulta2:
            print(f"{listado[persona]}     CONSULTA2")
            elim_paciente()
            consulta1 = False
    except:
        pass

    cons1_libre = str(input("Consulta nº1 libre: (pulsar s/n): "))
    cons2_libre = str(input("Consulta nº2 libre: (pulsar s/n): "))
    if cons1_libre == "s":
        consulta1 = True
    else:
        consulta1 = False
    if cons2_libre == "s":
        consulta2 = True
    else:
        consulta2 = False
    
    #print(f'--{consulta1} --{consulta2}')

    if len(listado) == 0 and consulta1 == True and consulta2 == True:
            print("El tiempo de consulta ha terminado.\nGracias por su visita.")
            break