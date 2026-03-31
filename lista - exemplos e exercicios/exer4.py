fila = ["ana","carlos","beatriz","daniel"]
atendido = []
fila.append("eduardo")
print(fila," estão na fila")

atendido.append(fila[0])
print(f"o cliente {atendido} foi atendido")

fila.remove(fila[0])
print(f"restam {fila} na fila")