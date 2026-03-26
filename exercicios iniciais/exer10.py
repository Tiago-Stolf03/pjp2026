nota=float(input("digite uma nota: "))
while nota>10 or nota<0:
    print("nota inválida, digite outra nota: ")
    nota=float(input())
if nota >=0 and nota<=10:
    print("Nota válida")

