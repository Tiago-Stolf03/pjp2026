
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

CREATE TABLE ____

---------------------------------------------------------------------------------

UPDATE ______ SET _____ = "___"

UPDATE ______ SET _____ = "___" WHERE _____ = ____

-----------------------------------------------------------------------------

SELECT _____ FROM _____ ORDER BY ____ 

SELECT _____ FROM _____ ORDER BY ____ ASC/DESC

SELECT _____ FROM _____ WHERE ____ LIKE "____" 

SELECT COUNT (_____) FROM _____

SELECT _____ , COUNT (____) FROM ____ GROUP BY ______

SELECT _____ , COUNT (____) FROM ____ JOIN _____ ON ______._______ = _____._____ GROUP BY ____.________

SELECT _____ , COUNT (____) FROM ____ JOIN _____ ON ______._______ = _____._____ GROUP BY ____.________ HAVING COUNT(_____) > _____
-------------------------------------------------------------------------------


 Comandos internos do shell sqlite3
(Executados diretamente no terminal do SQLite, começam com ponto)
 
Comando              Descrição
.tables              Lista todas as tabelas do banco
.schema              Mostra a estrutura (DDL) das tabelas
.headers on/off      Liga/desliga exibição de cabeçalhos
.mode column         Formata saída em colunas
.databases           Lista bancos de dados anexados
.quit                Sai do SQLite
 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 
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
renomeia                    RENAME             renomeia tabelas
conta                       COUNT              conta resgistros                      SELECT COUNT(*) AS total_clientes FROM clientes;
agrupa                      GROUP BY           filtro de agrupamento                 SELECT id_categoria, COUNT (1) FROM livro GROUP BY id_categoria
junta                       JOIN               integra registros na filtragem        SELECT nome_categoria, COUNT (1) FROM livro JOIN categoria ON categoria.id_categoria = livro.id_categoria GROUP BY livro.id_categoria

 
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Operadores comuns no WHERE
 
Operador                 Descrição                              Exemplo
=                        igualdade                              WHERE idade = 30
<> ou !=                 Diferente                              WHERE cidade <>'SãoPaulo'
> / < / >= / <=          Comparações numéricas                  WHERE salario > 3000
BETWEEN ... AND ...      Intervalo                              WHERE idade BETWEEN 18 AND 30
IN (...)                 Lista de valores                       WHERE estado IN ('SP', 'RJ', 'MG')
LIKE                     Correspondência com curingas (% e _)   WHERE nome LIKE 'Jo%'
IS NULL / IS NOT NULL    Valores nulos                          WHERE telefone IS NULL
AND / OR                 Combinação de condições                WHERE idade > 18 AND cidade = 'Rio'
 
--------------------------------------------------------------------------------------------------------------------------
 
 
Ordenação e Limite 
Sql
 
SELECT nome, idade
FROM clientes
WHERE idade >= 18
ORDER BY idade DESC
LIMIT 5;
ORDER BY: ordena os resultados (ASC crescente, DESC decrescente).
LIMIT: limita o número de linhas retornadas.
 
--------------------------------------------------------------------------------------------------
 
Agrupamento com filtro (GROUP BY + HAVING)
Sql
 
SELECT cidade, COUNT(*) AS total
FROM clientes
GROUP BY cidade
HAVING COUNT(*) > 10;
GROUP BY: agrupa registros.
HAVING: filtra grupos (diferente de WHERE, que filtra linhas antes do agrupamento).
 
---------------------------------------------------------------------------------------------------------------------
 
Exemplo completo
Sql
 
SELECT nome, idade, cidade
FROM clientes
WHERE idade BETWEEN 25 AND 40
  AND cidade IN ('São Paulo', 'Rio de Janeiro')
ORDER BY idade ASC
LIMIT 10 OFFSET 5;
 
OFFSET: pula as primeiras linhas (útil para paginação).

"""