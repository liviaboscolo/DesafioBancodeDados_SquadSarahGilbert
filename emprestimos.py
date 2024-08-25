import sqlite3
from datetime import datetime
import conexao as conn

def registrar_emprestimo(id_exemplar, id_usuario, data_emprestimo, prazo_devolucao):
    """
    Registra um novo empréstimo no banco de dados.
    
    :param id_exemplar: ID do exemplar emprestado
    :param id_usuario: ID do usuário que emprestou o livro
    :param data_emprestimo: Data em que o livro foi emprestado
    :param prazo_devolucao: Data até quando o livro deve ser devolvido
    """
    try:
        with conn.conexao:
            conn.cursor.execute('''
                INSERT INTO emprestimos (id_exemplar, id_usuario, data_emprestimo, prazo_devolucao)
                VALUES (?, ?, ?, ?)
            ''', (id_exemplar, id_usuario, data_emprestimo, prazo_devolucao))
        print(f"Empréstimo registrado: Exemplar {id_exemplar}, Usuário {id_usuario}")
    except sqlite3.IntegrityError as e:
        print(f"Erro ao registrar empréstimo: {e}")

def devolver_livro(id_exemplar, id_usuario):
    """
    Registra a devolução de um livro.
    
    :param id_exemplar: ID do exemplar devolvido
    :param id_usuario: ID do usuário que está devolvendo o livro
    """
    try:
        with conn.conexao:
            conn.cursor.execute('''
                UPDATE emprestimos
                SET data_devolucao = ?
                WHERE id_exemplar = ? AND id_usuario = ? AND data_devolucao IS NULL
            ''', (datetime.now().strftime('%Y-%m-%d'), id_exemplar, id_usuario))
        print(f"Devolução registrada: Exemplar {id_exemplar}, Usuário {id_usuario}")
    except sqlite3.Error as e:
        print(f"Erro ao registrar devolução: {e}")

def mostrar_emprestimos_em_atraso():
    """
    Mostra todos os empréstimos que estão em atraso.
    """
    data_atual = datetime.now().strftime('%Y-%m-%d')
    try:
        with conn.conexao:
            emprestimos_em_atraso = conn.cursor.execute('''
                SELECT id_exemplar, id_usuario, data_emprestimo, prazo_devolucao
                FROM emprestimos
                WHERE prazo_devolucao < ? AND data_devolucao IS NULL
            ''', (data_atual,)).fetchall()
            
            print("Empréstimos em atraso:")
            for emprestimo in emprestimos_em_atraso:
                print(f"Exemplar {emprestimo[0]}, Usuário {emprestimo[1]}, Data do Empréstimo {emprestimo[2]}, Prazo de Devolução {emprestimo[3]}")
    except sqlite3.Error as e:
        print(f"Erro ao consultar empréstimos em atraso: {e}")
