valor=(float(input("informe o valor gasto na compra: ")))
def gerar_pontos(valor_gasto):
    pontosdev=int(valor_gasto/5)
    return f"você ganhou {pontosdev} pontos pela sua compra"
print(gerar_pontos(valor))