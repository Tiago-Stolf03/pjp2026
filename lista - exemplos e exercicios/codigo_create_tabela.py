

 CREATE TABLE cliente
 (id_cliente INT PRIMARY KEY AUTO INCREMENT,
 nome_cliente VARCHAR(100) NOT NULL, telefone VARCHAR(50), endereco VARCHAR(50) NOT NULL, 
 cpf VARCHAR(50) NOT NULL 
 );


CREATE TABLE livro
 (id_livro INT PRIMARY KEY AUTO INCREMENT,
 nome_livro VARCHAR(100) NOT NULL, status VARCHAR(50) NOT NULL, id_editora INT, id_categoria INT,
 CONSTRAINT fk_livro_editora FOREIGN KEY (id_editora) REFERENCES editora(id_editora),
 CONSTRAINT fk_livro_categoria FOREING KEY (id_categoria) REFERENCES editora(id_editora)
 );


 CREATE TABLE categoria
 (id_categoria INT PRIMARY KEY AUTO INCREMENT,
 nome_categoria VARCHAR(100) NOT NULL, autor VARCHAR(50) NOT NULL, genero VARCHAR(50) NOT NULL );

 CREATE TABLE emprestimo
 (id_emprestimo INT PRIMARY KEY AUTO INCREMENT,
 nome_emprestimo VARCHAR(100) NOT NULL, id_cliente INT, id_livro INT, data_emprestimo VARCHAR(50), data_devolucao VARCHAR(50) 
 CONSTRAINT fk_emprestimo_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
 CONSTRAINT fk_emprestimo_livro FOREIGN KEY (id_livro) REFERENCES livro(id_livro)
 );

'''

 CREATE TABLE multa
 (id_multa INT PRIMARY KEY AUTO INCREMENT,
 nome_multa VARCHAR(100) NOT NULL,
 id_emprestimo VARCHAR(50) );


 CREATE TABLE editora
 (id_editora INT PRIMARY KEY AUTO INCREMENT,
 nome_editora VARCHAR(100) NOT NULL,
 );

 
""" 