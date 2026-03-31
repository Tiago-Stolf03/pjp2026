r=float(input("informe quantos reais você deseja converter: "))
def converter_dolar_real(d,r):
    d=r/5
    return d
d=converter_dolar_real(5,r)
if d>=1 and d<2:
    print("você converteu",r,"reais para ",d,"dólar")
else:
   print("você converteu",r,"reais para ",d,"dólares")