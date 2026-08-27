import math

calculadora = input("qual operação você vai querer fazer (+,-,*,/ ou raiz):  ")






if calculadora == "+":
    n1 = float(input("digite um numero: "))
    n2 = float(input("digite outro numero: "))
    print(n1+n2)

elif calculadora == "-":
    n1 = float(input("digite um numero: "))
    n2 = float(input("digite outro numero: "))
    print(n1-n2)

elif calculadora == "*":
    n1 = float(input("digite um numero: "))
    n2 = float(input("digite outro numero: "))
    print(n1*n2)

elif calculadora == "/":
    n1 = float(input("digite um numero: "))
    n2 = float(input("digite outro numero: "))
    print(n1/n2)

elif calculadora == "raiz":
    n1 = float(input("digite um numero: "))
    print(math.sqrt (n1))


else:
    print("operação invalida")




