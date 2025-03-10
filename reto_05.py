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