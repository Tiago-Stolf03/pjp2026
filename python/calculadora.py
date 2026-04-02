import tkinter as tk
from tkinter import messagebox
import funcao as f
valor1 =0
valor2 =0
result =0


 


def calcular(operacao):

    valor1= float(entry_valor1.get())

    valor2= float(entry_valor2.get())

    if operacao == "+":
        result=f.soma(valor1,valor2)
        entry_result.insert(0,result)
    elif operacao =="-":
        result=f.sub(valor1,valor2)
        entry_result.insert(0,result)
    elif operacao =="*":
        result=f.vezes(valor1,valor2)
        entry_result.insert(0,result)
    elif operacao =="/":
        result=f.div(valor1,valor2)
        entry_result.insert(0,result)
    return result
       
# Criando a janela
root = tk.Tk()
root.title("Calculadora")
root.geometry("1000x500")
 

# Configurando o espaçamento interno da janela
root.config(padx=350, pady=180)
 

# --- ELEMENTOS DA TELA ---
 
tk.Label(root, text="Valor1:").grid(row=0, column=0, sticky="w", pady=5)
entry_valor1 = tk.Entry(root, width=30)
entry_valor1.grid(row=0, column=1, pady=5)

"""
tk.Label(root, text="Operação:").grid(row=3, column=0, sticky="w", pady=5)
entry_operacao = tk.Entry(root, width=30)
entry_operacao.grid(row=3, column=1, pady=5)
"""

tk.Label(root, text="Valor2:").grid(row=1, column=0, sticky="w", pady=5)
entry_valor2 = tk.Entry(root, width=30)
entry_valor2.grid(row=1, column=1, pady=5)
 
tk.Label(root, text="resultado").grid(row=2, column=0, sticky="w", pady=5)
entry_result = tk.Entry(root, width=30)
entry_result.grid(row=2, column=1, pady=5)

btn_soma= tk.Button(root, text="+",command=lambda:(calcular("+")))
btn_soma.grid(row=3, column=0, pady=5, sticky="Ne")
btn_soma.config(width=5, height=2)

btn_sub= tk.Button(root, text="-",command=lambda:(calcular("-")))
btn_sub.grid(row=3, column=1, pady=5, sticky="W")
btn_sub.config(width=5, height=2)

btn_div= tk.Button(root, text="/",command=lambda:(calcular("/")))
btn_div.grid(row=4, column=0, pady=5, sticky="Ne")
btn_div.config(width=5, height=2)

btn_vezes= tk.Button(root, text="*",command=lambda:(calcular("*")))
btn_vezes.grid(row=4, column=1, pady=5, sticky="W")
btn_vezes.config(width=5, height=2)
  
root.mainloop()