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

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo (n - 1)
    
numero = int(input("Indica un numero entero para hallar su factorial: "))

resulatado = factorial_recursivo(numero)
print(f"El factorial de {numero} es {resulatado}")