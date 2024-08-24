import conexao as conn

# Tabela exemplares (necessária para emprestimos)
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS exemplares (
        id_exemplar INTEGER PRIMARY KEY,
        id_livro INTEGER,
        FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
    );
''')

# Tabela usuarios (necessária para emprestimos)
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY,
        id_pessoa INTEGER NOT NULL,
        telefone INTEGER NOT NULL,
        nacionalidade VARCHAR(200) NOT NULL,
        FOREIGN KEY (id_pessoa) REFERENCES pessoas(id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

# Tabela emprestimos
conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (
        id_emprestimo INTEGER PRIMARY KEY NOT NULL,
        id_exemplar INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        data_emprestimo DATE,
        data_devolucao DATE,
        data_devolvido DATE,
        FOREIGN KEY (id_exemplar) REFERENCES exemplares(id_exemplar) ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE NO ACTION ON UPDATE NO ACTION
    );
''')

# Confirmar as alterações e fechar a conexão
conn.conexao.commit()
conn.conexao.close()
