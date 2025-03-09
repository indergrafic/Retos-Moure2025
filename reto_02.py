def numeros(cad1, cad2):
    contador = 0
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{cad1} y {cad2}')
        elif i % 3 == 0:
            print(f'{cad1}')
        elif i % 5 == 0:
            print(f'{cad2}')
        else:
            contador +=1
            print(i)
    print(f"El numero se ha impreso {contador} veces")

numeros("uno", "dos")

