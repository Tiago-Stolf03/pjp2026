def validar_cupom(CAFE10,PROMO5):
    codigo=str(input("digite um código para obter desconto: "))
    if codigo=="CAFE10":
        return CAFE10
    if codigo=="PROMO5":
        return PROMO5
    else:
        return 0
codigo=validar_cupom(0.1,0.05)
print(codigo)


