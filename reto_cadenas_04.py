# #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */'''

fras1 = input("Introduce una palabra :")
fras2 = input("Introduce una segunda palabra :")

def palindro():
    palindromo = fras2[::-1]
    if fras1 == palindromo:
        print("Las palabras son palindromos.")
    else:
        print("No es un palindromo.")

def anagrama():
    ''' -sorted- ordena las palabras e indica si son iguales.'''
    print(f"{fras1} es anagrama de {fras2}: {sorted(fras1) == sorted(fras2)}")

def isograma():
    ''' Medimos la longitud de una palabra y el set de la otra 
    para comprobar si tienen el mismo numero de letras'''
    if len(fras1) == len(set(fras1)):
        print(f"La longitud de {fras1} es: {len(fras1)}\n\
y el set de {fras2} es: {len(set(fras2))}\n\
por lo tanto es un isogramas.")
    else:
        print(f"La palabra {fras1} no es un Isogramas.")
    if len(fras2) == len(set(fras2)):
        print(f"La longitud de {fras2} es: {len(fras2)}\n\
y el set de {fras2} es: {len(set(fras2))}\n\
por lo tanto es un isogramas.")
    else:
        print(f"La palabra {fras2} no es un Isogramas.")
    

            
palindro()
anagrama()
isograma()