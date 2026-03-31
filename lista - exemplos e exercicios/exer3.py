lista =[]

count=0
while count<5:
    numeros=float(input("digite um números "))
    count=count+1
    lista.append(numeros)

print("o maior valor é: ",max(lista))
print("o menor valor é: ",min(lista))
print("a soma é: ",sum(lista))

media = sum(lista)/count
print(f"a média final é: {media}")