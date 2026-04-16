
"""
 CREATE TABLE cliente
 (id_cliente INT PRIMARY KEY AUTO INCREMENT,
 nome_cliente VARCHAR(100) NOT NULL, telefone VARCHAR(50), endereco VARCHAR(50) NOT NULL, 
 cpf VARCHAR(50) NOT NULL 
 );

---------------------------------------------------------------------------------------------

CREATE TABLE livro
 (id_livro INT PRIMARY KEY AUTO INCREMENT,
 nome_livro VARCHAR(100) NOT NULL, status VARCHAR(50) NOT NULL, id_editora INT, id_categoria INT,
 CONSTRAINT fk_livro_categoria FOREING KEY (id_categoria) REFERENCES editora(id_categoria)
 );

-----------------------------------------------------------------------------------------

 CREATE TABLE categoria
 (id_categoria INT PRIMARY KEY AUTO INCREMENT,
 nome_categoria VARCHAR(100) NOT NULL, autor VARCHAR(50) NOT NULL, genero VARCHAR(50) NOT NULL 
 );

--------------------------------------------------------------------------------------------------------

 CREATE TABLE emprestimo
 (id_emprestimo INT PRIMARY KEY AUTO INCREMENT,
 nome_emprestimo VARCHAR(100) NOT NULL, id_cliente INT, id_livro INT, data_emprestimo VARCHAR(50), data_devolucao VARCHAR(50), 
 CONSTRAINT fk_emprestimo_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
 CONSTRAINT fk_emprestimo_livro FOREIGN KEY (id_livro) REFERENCES livro(id_livro)
 );

---------------------------------------------------------------------------------------

 CREATE TABLE multa
 (id_multa INT PRIMARY KEY AUTO INCREMENT,
 nome_multa VARCHAR(100) NOT NULL, id_emprestimo VARCHAR(50), 
 CONSTRAINT fk_multa_emprestimo FOREIGN KEY (id_emprestimo) REFERENCES emprestimo(id_emprestimo)
 );

-------------------------------------------------------------------------------

 CREATE TABLE editora
 (id_editora INT PRIMARY KEY AUTO INCREMENT,
 nome_editora VARCHAR(100),
 );

"""
-------------------------------------------------------------------------
"""

                         ALTER 

ALTER TABLE ____ RENAME TO ____
ALTER TABLE ____ RENAME COLUMN ____ TO ____

--------------------------------------------------------------------------------
INSERT INTO ____ (_____) VALUES ("___")

---------------------------------------------------------------------------------
                          DELETE

DELETE FROM ____ 

DELETE FROM ____ WHERE ____ = N/POSIÇÃO

DELETE FROM ____ WHERE ____ IN ( _,_,_,... )

---------------------------------------------------------------------------------

DROP TABLE ____

------------------------------------------------------------------------------

CREATE TABLE ____

---------------------------------------------------------------------------------

UPDATE ______ SET _____ = "___"

UPDATE ______ SET _____ = "___" WHERE _____ = ____




Comandos SQL no SQLite
 
Categoria                   Comando            Descrição                             Exemplo


Criar tabela                CREATE TABLE       Cria uma nova tabela                  CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER);

Excluir tabela              DROP TABLE         Remove uma tabela existente           DROP TABLE clientes;

Alterar tabela              ALTER TABLE        Adiciona ou renomeia colunas          ALTER TABLE clientes ADD COLUMN email TEXT;

Inserir dados               INSERT INTO        Insere registros                      INSERT INTO clientes (nome, idade) VALUES ('Ana', 30);

Selecionar dados            SELECT             Consulta registros                    SELECT nome, idade FROM clientes;

Atualizar dados             UPDATE             Modifica registros existentes         UPDATE clientes SET idade = 31 WHERE id = 1;

Excluir dados               DELETE             Remove registros                      DELETE FROM clientes WHERE id = 1;

Ordenar resultados          ORDER BY           Ordena resultados                     SELECT * FROM clientes ORDER BY idade DESC;

Filtrar resultados          WHERE              Aplica condições                      SELECT * FROM clientes WHERE idade > 25;

Limitar resultados          LIMIT              Restringe quantidade de linhas        SELECT * FROM clientes LIMIT 5;

Relacionar tabelas          JOIN               Une dados de tabelas                  SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id;

Chave estrangeira           FOREIGN KEY        Define relacionamento                 FOREIGN KEY(cliente_id) REFERENCES clientes(id)


Comandos internos do shell sqlite3
 
Comando                Descrição
.tables                Lista todas as tabelas do banco
.schema                Mostra a estrutura (DDL) das tabelas
.headers on/off        Liga/desliga exibição de cabeçalhos
.mode column           Formata saída em colunas
.databases            Lista bancos de dados anexados
.quit                  Sai do SQLite

"""