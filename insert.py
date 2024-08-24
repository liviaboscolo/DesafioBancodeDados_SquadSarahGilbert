import conexao as conn

# Inserção de dados na tabela livros
conn.cursor.execute('''
    INSERT INTO livros (id_livro, titulo, editora, num_max_renovacoes) VALUES
        (1, "The StatQuest Illustrated Guide to Machine Learning!!!", "Packt Publishing", 3),
        (2, "Código Limpo: Habilidades Práticas do Agile", "Alta Books", 4),
        (3, "Introdução à Programação com Python", "Novatec", 3),
        (4, "Python para Data Science", "Alta Books", 2),
        (5, "Algoritmos e Programação de Computadores", "GEN LTC", 4);
''')

# Inserção de dados na tabela generos
conn.cursor.execute('''
    INSERT INTO generos (id_genero, nome) VALUES
        (1, "Programação"),
        (2, "Aprendizado de máquina"),
        (3, "Python");
''')

# Inserção de dados na tabela livros_generos
conn.cursor.execute('''
    INSERT INTO livros_generos (id_livro, id_genero) VALUES
        (1, 2),
        (2, 1),
        (5, 1),
        (3, 3),
        (4, 3);
''')

# Inserção de dados na tabela exemplares
conn.cursor.execute('''
    INSERT INTO exemplares (id_exemplar, id_livro) VALUES
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 4),
        (7, 4),
        (8, 5),
        (9, 5),
        (10, 5),
        (11, 5);
''')

# Inserção de dados na tabela pessoas
conn.cursor.execute('''
    INSERT INTO pessoas (id_pessoa, nome, email) VALUES
        (1, "Jéssica Lizar", "jessicalizar@gmail.com"),
        (2, "Letícia Almeida", "leticiaalmeida@gmail.com"),
        (3, "Lívia Boscolo", "liviaboscolo@gmail.com"),
        (4, "Michelle Martins", "michellemartins@gmail.com"),
        (5, "Nadiveth Duno", "nadivethduno@gmail.com"),
        (6, "Raquel Maia", "raquelmaia@gmail.com"),
        (7, "Rosana Francisco", "rosanafrancisco@gmail.com"),
        (8, "Josh Starmer", "joshstarmer@gmail.com"),
        (9, "Robert C. Martin", "robertmartin@gmail.com"),
        (10, "Nilo Ney Coutinho", "neycoutinho@gmail.com"),
        (11, "Henrique Bastos", "henriquebastos@gmail.com"),
        (12, "An Engelbrecht", "anengelbrecht@gmail.com"),
        (13, "Gilberto Nakamiti", "gilbertonakamiti@gmail.com"),
        (14, "Dilermando Junior", "dilermandojr@gmail.com");
''')

# Inserção de dados na tabela usuarios
conn.cursor.execute('''
    INSERT INTO usuarios (id_usuario, id_pessoa, telefone, nacionalidade) VALUES
        (1, 1, "12345678910", "Brasileira"),
        (2, 2, "10987654321", "Brasileira"),
        (3, 3, "12345109876", "Brasileira"),
        (4, 4, "10987612345", "Brasileira"),
        (5, 5, "678910123456", "Venezuelana"),
        (6, 6, "54321109876", "Brasileira"),
        (7, 7, "54321678923", "Brasileira");
''')

# Inserção de dados na tabela autores
conn.cursor.execute('''
    INSERT INTO autores (id_autor, id_pessoa) VALUES
        (1, 8),
        (2, 9),
        (3, 10),
        (4, 11),
        (5, 12),
        (6, 13),
        (7, 14);
''')

# Inserção de dados na tabela autores_livros
conn.cursor.execute('''
    INSERT INTO autores_livros (id_autor, id_livro, id_pessoa) VALUES
        (1, 1, 8),
        (2, 2, 9),
        (3, 3, 10),
        (4, 4, 11),
        (5, 5, 12),
        (6, 5, 13),
        (7, 5, 14);
''')

# Inserção de dados na tabela emprestimos
conn.cursor.execute('''
    INSERT INTO emprestimos (id_exemplar, id_usuario, DataEmprestimo, DataDevolucao, DataDevolvido) VALUES
        (1, 1, '2024-08-20', '2024-08-27', NULL),
        (2, 2, '2024-08-21', '2024-08-28', '2024-08-28'),
        (3, 3, '2024-08-22', '2024-08-29', NULL),
        (4, 4, '2024-08-23', '2024-08-30', NULL),
        (5, 5, '2024-08-24', '2024-08-31', NULL);
''')

# Confirma as mudanças e fecha a conexão
conn.conexao.commit()
conn.conexao.close()
