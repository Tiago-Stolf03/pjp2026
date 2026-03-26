preco_unitario=float(input("digite o valor do produto: "))
quantidade=int(input("informe a quantidade de produtos: "))
def calcular_item(preco_unitario,quantidade):
    total=(preco_unitario*quantidade) + (preco_unitario*quantidade*0.05)
    return total
print(calcular_item(preco_unitario, quantidade))