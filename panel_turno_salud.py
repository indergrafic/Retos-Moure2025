"""
El programa trata de emular el panel existente en los edificios de salud en el
que se nos indica cuando nos corresponde el turno, con la informacion siguiente:
    - Un conjunto de dos letas y un numero, ejm.: Y5J. Esta es la misma que el tique que tenemos.
    Este código es aleatorio e individual.
    - Y la cunsulta que nos corresponde, ejm.: Consulta 1.
"""

cod_letras = {"a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "y", "z"}
cod_num = {"1", "2", "3","4", "5", "6", "7", "8", "9", "0"}

consulta1: int = 0
consulta2: int = 0

persona = int(input("Indique su DNI(4 primeros numeros): "))

cod_paciente = ()
listado = {}
def turno():
    while True:
        if persona in listado:
            print(f'Usted ya esta en lista de espera, su codigo es {listado[persona]}')
        else:
            letra1 = cod_letras[5]
            cod_paciente.append(letra1)
            num = cod_num[6]
            cod_paciente.append(num)
            letra2 = cod_letras[15]
            cod_paciente.append(letra2)
            listado[persona] = cod_paciente
        for i in listado.values():
            if  i == cod_paciente:
                pass