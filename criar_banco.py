import sqlite3

# Conecta ao arquivo (ele será criado automaticamente)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 1. Cria a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS frota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL,
        numero_frota TEXT NOT NULL,
        horas INTEGER NOT NULL,
        status TEXT NOT NULL
    )
''')

# 2. Dados iniciais que tínhamos antes
dados_iniciais = [
    ("Colhedora CH570", "40024", 600, "Manutenção Requerida"),
    ("Trator 8R", "30015", 480, "Operacional"),
    ("Pulverizador M4040", "20088", 150, "Operacional")
]

# 3. Insere os dados
cursor.executemany('''
    INSERT INTO frota (modelo, numero_frota, horas, status) 
    VALUES (?, ?, ?, ?)
''', dados_iniciais)

conn.commit()
conn.close()
print("✅ Arquivo database.db criado com sucesso com os dados iniciais!")