import sqlite3

def criar_banco():
    conexao = sqlite3.connect("BDcompra.db")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar (50) NOT NULL,
            telefone INTEGER NOT NULL);
""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_produto VARCHAR(20) NOT NULL,
            cor_produto VARCHAR(20) NOT NULL,
            valor_produto REAL NOT NULL);
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venda(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cadastro_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        data_venda DATE NOT NULL,
        FOREIGN KEY (cadastro_id) REFERENCES cadastro (id),
        FOREIGN KEY (produto_id) REFERENCES produto (id));
""")

    conexao.commit()
    conexao.close()
    print("Banco criado com sucesso.")

if __name__ == "__main__":
    criar_banco()