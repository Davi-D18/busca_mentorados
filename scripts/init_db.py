from configs.database import get_db_connection


class DBInitializer:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS mentoreados (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS encontros (
            id INTEGER PRIMARY KEY,
            mentoreado_id INTEGER,
            data TEXT,
            confirmou_presenca INTEGER,
            FOREIGN KEY (mentoreado_id) REFERENCES mentoreados(id)
        )''')

    def insert_mentoreados(self):
        self.cursor.executemany('INSERT OR IGNORE INTO mentoreados VALUES (?,?,?)', [
            (1, 'Gertrudes Silva', 'gertrudes@email.com'),
            (2, 'José Costa', 'jose@email.com'),
            (3, 'Genoveva Souza', 'genoveva@email.com'),
            (4, 'Matias Lima', 'matias@email.com'),
            (5, 'Maria Martins', 'maria@email.com'),
        ])

    def insert_encontros(self):
        self.cursor.executemany('INSERT OR IGNORE INTO encontros VALUES (?,?,?,?)', [
            (1, 1, '2026-04-01', 1),
            (2, 1, '2026-04-08', 1),
            (3, 2, '2026-04-01', 0),
            (4, 3, '2026-04-08', 1),
            (5, 2, '2026-04-08', 1),
        ])

    def run(self):
        self.create_tables()
        self.insert_mentoreados()
        self.insert_encontros()
        self.close()
        print("✅ Banco de dados criado com sucesso!")
