# #05 VALOR Y REFERENCIA
> #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */'''
 
 
def fun_valor(num1: int, num2: int):
    temp = num1
    num1 = num2
    num2 = temp   
    return num1, num2

def fun_refe(num1: list, num2: list):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

var_valor_1 = 5
var_valor_2 = 10

ref1 = [5, 10]
ref2 = [15,30]

var_valor_3, var_valor_4 = fun_valor(var_valor_1, var_valor_2)
print(f"{var_valor_1} - {var_valor_2}")
print(f"{var_valor_3} - {var_valor_4}\n\n")

ref3, ref4 = fun_refe(ref1, ref2)
print(f"{ref1} - {ref2}")
print(f"{ref3} - {ref4}")