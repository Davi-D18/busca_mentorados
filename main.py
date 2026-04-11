from scripts.init_db import DBInitializer

print("Iniciando a criação do banco de dados...")
db = DBInitializer()
db.run()
