temp_entrada=float(input("digite a temperatura atual da caldeira: "))

def temperatura_maquina(temp_atual):
    if temp_atual<90:
        return "aquecendo"
    elif temp_atual>=90 and temp_atual<=100:
        return "pronta para uso"
    else:
        return "PERIGO, superaquecimento"
print(temperatura_maquina(temp_entrada))
