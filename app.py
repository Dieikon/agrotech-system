import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

def conectar_banco():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def iniciar_banco():
    conn = conectar_banco()
    
    # 1. NOVA TABELA: Operadores
    conn.execute('''
        CREATE TABLE IF NOT EXISTS operador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    
    # 2. TABELA FROTA: Agora conectada ao Operador pelo ID
    conn.execute('''
        CREATE TABLE IF NOT EXISTS frota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            numero_frota TEXT NOT NULL,
            operador_id INTEGER,
            FOREIGN KEY (operador_id) REFERENCES operador (id)
        )
    ''')
    
    # 3. TABELA TELEMETRIA (Alinhamento corrigido aqui!)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS telemetria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maquina_id INTEGER NOT NULL,
            nivel_oleo_motor REAL NOT NULL,
            nivel_oleo_hidraulico REAL NOT NULL,
            oleo_diesel REAL NOT NULL,  -- ESSA É A LINHA NOVA!
            temp_motor REAL NOT NULL,
            status_operacao TEXT NOT NULL,
            toneladas_hora REAL DEFAULT 0.0,
            data_leitura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (maquina_id) REFERENCES frota (id)
        )
    ''')

    # INJETANDO OPERADORES DE TESTE
    qtd_operadores = conn.execute('SELECT COUNT(*) FROM operador').fetchone()[0]
    if qtd_operadores == 0:
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Marcos Silva', '(11) 99999-1111')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('João Batista', '(11) 98888-2222')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Ricardo Souza', '(11) 97777-3333')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Paulo Souza', '(11) 97765-4444')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Victor Souza', '(11) 97997-5555')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Junior Souza', '(11) 98577-6666')")
        conn.execute("INSERT INTO operador (nome, telefone) VALUES ('Marlon Souza', '(11) 97725-7777')")
        
    conn.commit()
    conn.close()

# O iniciar_banco() fica totalmente colado no canto esquerdo (Zero espaços)
iniciar_banco()

@app.route('/')
def home():
    conn = conectar_banco()
    
    # Fazemos um JOIN: Junta a tabela de Frota com a de Operadores para pegar o nome e telefone reais
    frota = conn.execute('''
        SELECT frota.id, frota.modelo, frota.numero_frota, 
               operador.nome AS operador_nome, operador.telefone AS operador_telefone
        FROM frota
        LEFT JOIN operador ON frota.operador_id = operador.id
    ''').fetchall()
    
    # Busca os operadores para mostrar no "Dropdown" do formulário
    operadores = conn.execute('SELECT * FROM operador').fetchall()
    
    conn.close()
    return render_template('index.html', maquinas=frota, operadores=operadores)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    modelo = request.form.get('modelo')
    numero_frota = request.form.get('numero_frota')
    operador_id = request.form.get('operador_id')
    
    conn = conectar_banco()
    conn.execute('INSERT INTO frota (modelo, numero_frota, operador_id) VALUES (?, ?, ?)',
                 (modelo, numero_frota, operador_id))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/excluir/<int:id>')
def excluir(id):
    conn = conectar_banco()
    conn.execute('DELETE FROM frota WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = conectar_banco()
    
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        numero_frota = request.form.get('numero_frota')
        operador_id = request.form.get('operador_id')
        
        conn.execute('''
            UPDATE frota 
            SET modelo = ?, numero_frota = ?, operador_id = ? 
            WHERE id = ?
        ''', (modelo, numero_frota, operador_id, id))
        
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    
    maquina = conn.execute('SELECT * FROM frota WHERE id = ?', (id,)).fetchone()
    operadores = conn.execute('SELECT * FROM operador').fetchall()
    conn.close()
    return render_template('editar.html', maquina=maquina, operadores=operadores, id=id)

@app.route('/maquina/<int:id_maquina>/dashboard')
def dashboard_maquina(id_maquina):
    conn = conectar_banco()
    maquina = conn.execute('SELECT * FROM frota WHERE id = ?', (id_maquina,)).fetchone()
    if not maquina:
        conn.close()
        return "Máquina não encontrada no sistema", 404
        
    telemetria = conn.execute('SELECT * FROM telemetria WHERE maquina_id = ? ORDER BY data_leitura DESC LIMIT 1', (id_maquina,)).fetchone()
    conn.close()
    return render_template('dashboard_maquina.html', maquina=maquina, telemetria=telemetria)

@app.route('/relatorio')
def relatorio():
    conn = conectar_banco()
    total_maquinas = conn.execute('SELECT COUNT(*) FROM frota').fetchone()[0]
    conn.close()
    return render_template('relatorio.html', total=total_maquinas, alerta=0, operacionais=total_maquinas, disponibilidade=100)

if __name__ == '__main__':
    app.run(debug=True)