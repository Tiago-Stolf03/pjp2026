import tkinter as tk
from tkinter import messagebox
import funcao_usuario as f
import sqlite3


def conectar():
        conn = sqlite3.connect("./bancodedados/banco.db")
        cursor = conn.cursor()
        cursor.execute ("")
        conn.commit()  
        conn.close()
        return conn 
 
def autenticar_dados():
    login = entry_login.get()
    senha = entry_senha.get()
    if  login == "abc" and senha == "123":
        messagebox.showinfo("Sucesso", "Login realizado!")
        root.destroy()
        import principal
    elif login != "abc" and senha != "123":
        mostradados = f.mostra()
        messagebox.showwarning("ERRO", f"{mostradados}")

# Criando a janela
root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("350x200")
 
# Configurando o espaçamento interno da janela
root.config(padx=20, pady=20)
 
# --- ELEMENTOS DA TELA ---
 
# Linha 0: login
tk.Label(root, text="Login:").grid(row=0, column=0, sticky="w", pady=5)
entry_login = tk.Entry(root, width=30)
entry_login.grid(row=0, column=1, pady=5)
 
# Linha 1: senha
tk.Label(root, text="Senha:").grid(row=1, column=0, sticky="w", pady=5)
entry_senha = tk.Entry(root, width=30)
entry_senha.grid(row=1, column=1, pady=5)
 
# Linha 2: Botão (Ocupando duas colunas)
btn_salvar = tk.Button(root, text="Confirmar Cadastro", command=autenticar_dados)
btn_salvar.grid(row=2, column=0, columnspan=2, pady=20)
 
root.mainloop()