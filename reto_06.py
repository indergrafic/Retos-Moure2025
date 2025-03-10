''' Ejercicio '''

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