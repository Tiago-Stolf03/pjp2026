frutas = ["abacate","banana","maçã"]
frutas.append("laranja")      #adiciona no final da lista
print(frutas)
frutas.insert(1,"cereja")     #adiciona na posição correspondente e empurra o resto da lista para o lado
print(frutas)

print(frutas[0])              #printa apenas o item da posição mencionada
frutas.remove("cereja")       #remove o item especificado 
print(frutas)

frutas[3] = "amora"           #altera o item na posição correspondente por um novo
print(frutas)


tamanho = len(frutas)         #informa o tamanho da lista
print(tamanho)

for fruta in frutas:
    print(f"eu gosto de {fruta}")