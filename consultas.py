import sqlite3
from datetime import datetime  # Importação do módulo datetime
import conexao as conn

def print_consulta(consulta):
    for row in consulta:
        print(row)

##############################################################################
# Listar todos os livros disponíveis. | Raquel
##############################################################################
print('Listar todos os livros disponíveis: ')
list_books = conn.cursor.execute('''
    SELECT titulo 
    FROM livros 
    WHERE id_livro NOT IN (
        SELECT id_livro 
        FROM exemplares 
        WHERE id_exemplar IN (
            SELECT id_exemplar 
            FROM emprestimos 
            WHERE data_devolucao IS NULL
        )
    )
''')
print_consulta(list_books)

##############################################################################
# Encontrar todos os livros emprestados no momento. | Livia
##############################################################################
print('\nEncontrar todos os livros emprestados no momento: ')
loan_cursor = conn.cursor.execute('''
    SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao
    FROM emprestimos
    LEFT JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
    LEFT JOIN livros ON exemplares.id_livro = livros.id_livro
    LEFT JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
    WHERE emprestimos.data_devolucao IS NULL
''')
loan_results = loan_cursor.fetchall()

if loan_results:
    print_consulta(loan_results)

##############################################################################
# Verificar o número de cópias disponíveis de um determinado livro. | Jéssica
##############################################################################
print('\nVerificar o número de cópias disponíveis de um determinado livro: ')
var_id_livro = 5  # Alterar conforme necessário

# Consulta para verificar o número de exemplares
check_exemplares = conn.cursor.execute(f'''
    SELECT COUNT(*)
    FROM exemplares
    WHERE id_livro = {var_id_livro}
''')
total_copias = check_exemplares.fetchone()[0]

# Consulta para verificar o número de exemplares emprestados
check_emprestados = conn.cursor.execute(f'''
    SELECT COUNT(*)
    FROM emprestimos
    JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
    WHERE exemplares.id_livro = {var_id_livro} AND emprestimos.data_devolucao IS NULL
''')
emprestados = check_emprestados.fetchone()[0]

# Número de cópias disponíveis
disponiveis = total_copias - emprestados
print(f'- Livro id: {var_id_livro}\n- Cópias disponíveis: {disponiveis}')

##############################################################################
# Mostrar os empréstimos em atraso. | Rosana
##############################################################################
print('\nMostrar os empréstimos em atraso: ')
data_atual = datetime.now().strftime('%Y-%m-%d')  # Usando datetime para obter a data atual
emprestimos_atraso = conn.cursor.execute('''
    SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.prazo_devolucao
    FROM emprestimos
    JOIN exemplares ON emprestimos.id_exemplar = exemplares.id_exemplar
    JOIN livros ON exemplares.id_livro = livros.id_livro
    WHERE emprestimos.prazo_devolucao < ? AND emprestimos.data_devolucao IS NULL
''', (data_atual,))

print("Empréstimos em atraso:")
print_consulta(emprestimos_atraso)

# Fechar a conexão
conn.conexao.commit()
conn.conexao.close()
