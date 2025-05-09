# #06 RECURSIVIDAD
#### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
'''

def countdown(numero: int):
    if numero >= 0:
        print(numero)
        countdown(numero - 1)

countdown(50)

'''Calcular el factorial de un numero con una funcion recursiva'''

def factorial(num: int):
    if num < 0:
        print("Los números negativos no son validos")
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(5))


'''Serie Fibonacci de forma recursiva'''

def fibonacci_recursivo(n: int):
    if n <= 0:
        print("La posicion tiene que ser mayor de cero")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
print(fibonacci_recursivo(7))