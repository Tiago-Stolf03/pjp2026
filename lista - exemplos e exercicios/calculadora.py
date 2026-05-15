# INFORMAÇÕES DO CÓDIGO
# e = expoente / elevado ,   r = raiz
# y = yes ,   n = no

#ATENÇÃO!!! Se você deseja tirar a raiz tenha em mente uma coisa:
# Só é possível tirar a raiz QUADRADA, NÃO é posssível tirar raiz cúbica,quarta,quinta,... 

continuar = "y"
num1 = float(input("digite um número: "))
sinal = str(input("digite um sinal matemático (+, -, *, /, e, r): "))
if sinal == "r":
    resultado = num1 **0.5
    print(resultado)

    continuar = str(input("deseja continuar ( y/n): "))

    while continuar == "y":
        sinal = str(input("digite um sinal matemático (+, -, *, /, e, r): "))
        if sinal == "r":
              print("tenha em mente que o número digitado será o valor que será obtida a raiz quadrada")
        num1 = float(input("digite um número: "))
        if sinal == "+":
                resultado = resultado + num1
                print(resultado)
        elif sinal == "-":
                resultado = resultado - num1
                print(resultado)
        elif sinal == "*":
                resultado = resultado * num1
                print(resultado)
        elif sinal == "/":
                resultado = resultado / num1
                print(resultado)
        elif sinal == "e":
                resultado = resultado ** num1
                print(resultado)
        elif sinal == "r":
                num1 = num1 ** 0.5
                print(num1)

        continuar = str(input("deseja continuar ( y/n): "))


if sinal != "r" and continuar == "y":
    num2 = float(input("digite um número: "))
    resultado = float()
    if sinal == "+":
            resultado = num1 + num2
            print(resultado)
    elif sinal == "-":
            resultado = num1 - num2
            print(resultado)
    elif sinal == "*":
            resultado = num1 * num2
            print(resultado)
    elif sinal == "/":
            resultado = num1 / num2
            print(resultado)
    elif sinal == "e":
            resultado = num1 ** num2
            print(resultado)
    

    continuar = str(input("deseja continuar ( y/n): "))

    while continuar == "y":
        sinal = str(input("digite um sinal matemático (+, -, *, /, e, r): "))
        if sinal == "r":
              print("tenha em mente que o número digitado será o valor que será obtida a raiz quadrada")
        num1 = float(input("digite um número: "))
        if sinal == "+":
            resultado = resultado + num1
            print(resultado)
        elif sinal == "-":
            resultado = resultado - num1
            print(resultado)
        elif sinal == "*":
            resultado = resultado * num1
            print(resultado)
        elif sinal == "/":
            resultado = resultado / num1
            print(resultado)
        elif sinal == "e":
            resultado = resultado ** num1
            print(resultado)
        elif sinal == "r":
            num1 = num1**0.5
            print(num1)

        continuar = str(input("deseja continuar ( y/n): "))



