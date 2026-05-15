import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("./bancodedados/banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livro (
            id_livro INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_livro VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    return conn

# --- LÓGICA DAS TELAS ---

def obter_categorias():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_categoria, nome_categoria FROM categoria")
    dados = cursor.fetchall()
    conn.close()
    return dados

def abrir_cadastro(parent, id_livro=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar livro" if id_livro else "Cadastrar livro")
    janela_cad.geometry("350x200")
    
    tk.Label(janela_cad, text="Nome do livro:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    # Campo: Seleção de Categoria (Combobox)
    tk.Label(janela_cad, text="Selecione a categoria:").pack(pady=(15, 5))

    # Buscamos as categorias do banco
    lista_categorias = obter_categorias() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]


    # Criamos uma lista apenas com os nomes para exibir no Combobox

    nomes_categorias = [c[1] for c in lista_categorias]

    combo_categoria = ttk.Combobox(janela_cad, values=nomes_categorias, width=32, state="readonly")

    combo_categoria.pack()

    # Se for EDIÇÃO, preenche o campo com o nome atual
    if id_livro:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_livro FROM livro WHERE id_livro = ?", (id_livro,))
        resultado = cursor.fetchone()
        if resultado:
            ent_nome.insert(0, resultado[0])
        conn.close()
    
    def salvar():
        nome = ent_nome.get()
        if not nome.strip():
            messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if id_livro:
            # Lógica de Atualização
            cursor.execute("UPDATE livro SET nome_livro = ? WHERE id_livro = ?", (nome, id_livro))
            mensagem = "Livro atualizado com sucesso!"
        else:
            # Lógica de Inserção
            cursor.execute("INSERT INTO livro (nome_livro) VALUES (?)", (nome,))
            mensagem = "Livro cadastrado com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if id_livro else "Salvar"
    btn_cor = "#00ff55" if id_livro else "lightgreen"
    
    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

def abrir_consulta(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar Livros")
    janela_con.geometry("500x480") 

    # 1. Tabela (Treeview)
    colunas = ("ID", "Nome do Livro")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome do livro", text="Nome do livro")
    tabela.column("ID", width=100, anchor="center")
    tabela.pack(pady=70, padx=50, fill="both", expand=True)

    # 2. Função interna para o botão Editar
    def executar_edicao():
        item_selecionado = tabela.selection()
        
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um livro na lista!")
            return

        valores = tabela.item(item_selecionado, "values")
        id_liv = valores[0]

        # Abre a mesma tela de cadastro, mas agora enviando o ID para modo edição
        abrir_cadastro(parent, id_livro=id_liv)
        janela_con.destroy() 

    # 3. Botões de Ação
    frame_botoes = tk.Frame(janela_con)
    frame_botoes.pack(pady=10)

    btn_editar = tk.Button(
        frame_botoes, 
        text="Editar Selecionada", 
        command=executar_edicao,
        bg="#3e538a",
        font=("Arial", 10, "bold"),
        width=50
    )
    btn_editar.pack(side="left", padx=5)

    # 4. Buscar dados iniciais
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livro")
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    conn.close()
