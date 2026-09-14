import sqlite3

def criar_banco():
    #serve para conectar ou criar o  banco
    conexao = sqlite3.connect("teste1.db")
    cursor = conexao.cursor()

    #ativando checagem de chave estrangeira 
    cursor.execute("PRAGMA foreign_keys = ON")

    #criando primeira tabela de cadastro
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR (50) NOT NULL,
            telefone INTEGER,
            endereco VARCHAR (100)
        );
    """)

    #criando segunda entidade filha 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            valor REAL NOT NULL,
            tipo VARCHAR(50) NOT NULL,
            cadastro_id INTEGER NOT NULL,
            FOREIGN KEY (cadastro_id) REFERENCES cadastro (id) ON DELETE CASCADE
        );
    """)

    #SALVAR E ENCERRAR A CONEXÃO 
    conexao.commit()
    conexao.close()
    print("Banco de dados configurado com sucesso.")

if __name__ == "__main__":
    criar_banco()


    