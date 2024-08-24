import conexao as conn

##############################################################################
# Atualizar | Jéssica
##############################################################################

# Atualizar o número máximo de renovações de um livro
novo_num_max_renovacoes = 5
id_livro = 1
conn.cursor.execute('''
    UPDATE livros
    SET num_max_renovacoes = ?
    WHERE id_livro = ?
''', (novo_num_max_renovacoes, id_livro))
print(f"Livro com ID {id_livro} atualizado com novo número máximo de renovações: {novo_num_max_renovacoes}")

##############################################################################
# Excluir | Nadi
##############################################################################
# Excluir tabelas
conn.cursor.execute('DROP TABLE IF EXISTS livros')
conn.cursor.execute('DROP TABLE IF EXISTS generos')
conn.cursor.execute('DROP TABLE IF EXISTS livros_generos')
conn.cursor.execute('DROP TABLE IF EXISTS exemplares')
conn.cursor.execute('DROP TABLE IF EXISTS pessoas')
conn.cursor.execute('DROP TABLE IF EXISTS usuarios')
conn.cursor.execute('DROP TABLE IF EXISTS autores')
conn.cursor.execute('DROP TABLE IF EXISTS autores_livros')
conn.cursor.execute('DROP TABLE IF EXISTS emprestimos')

# Excluir um autor específico
id_autor = 7
conn.cursor.execute('''
    DELETE FROM autores
    WHERE id_autor = ?
''', (id_autor,))
print(f"Autor com ID {id_autor} excluído.")

conn.conexao.commit()
conn.conexao.close()
