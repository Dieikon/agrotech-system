import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função para conectar ao banco
def conectar_banco():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # Permite acessar colunas pelo nome
    return conn

# Criar a tabela se ela não existir
def iniciar_banco():
    conn = conectar_banco()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS frota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            numero_frota TEXT NOT NULL,
            horas INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

iniciar_banco()

# Criamos a lista fora da função para que ela não resete toda vez
frota = [
    {"modelo": "Colhedora CH570", "numero_frota": "40024", "horas": 600, "status": "Manutenção Requerida"},
    {"modelo": "Trator 8R", "numero_frota": "30015", "horas": 480, "status": "Operacional"},
    {"modelo": "Pulverizador M4040", "numero_frota": "20088", "horas": 150, "status": "Operacional"}
]

@app.route('/')
def home():
    conn = conectar_banco()
    # Busca todas as máquinas do banco de dados
    frota = conn.execute('SELECT * FROM frota').fetchall()
    conn.close()
    return render_template('index.html', maquinas=frota)

# Rota para Cadastrar
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    modelo = request.form.get('modelo')
    numero_frota = request.form.get('numero_frota')
    horas = int(request.form.get('horas'))
    status = "Manutenção Requerida" if horas >= 600 else "Operacional"
    
    conn = conectar_banco()
    conn.execute('INSERT INTO frota (modelo, numero_frota, horas, status) VALUES (?, ?, ?, ?)',
                 (modelo, numero_frota, horas, status))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Rota para Excluir
@app.route('/excluir/<int:id>')
def excluir(id):
    conn = conectar_banco()
    conn.execute('DELETE FROM frota WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Rota para Editar (Prepara os dados para o formulário)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = conectar_banco()
    
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        numero_frota = request.form.get('numero_frota')
        horas = int(request.form.get('horas'))
        status = "Manutenção Requerida" if horas >= 600 else "Operacional"
        
        # O banco tenta escrever aqui. Ele precisa estar "destravado"
        conn.execute('''
            UPDATE frota 
            SET modelo = ?, numero_frota = ?, horas = ?, status = ? 
            WHERE id = ?
        ''', (modelo, numero_frota, horas, status, id))
        
        conn.commit()
        conn.close()  # FECHA AQUI APÓS SALVAR
        return redirect(url_for('home'))
    
    # Se for apenas carregar a página (GET)
    maquina = conn.execute('SELECT * FROM frota WHERE id = ?', (id,)).fetchone()
    conn.close() # FECHA AQUI APÓS LER
    return render_template('editar.html', maquina=maquina, id=id)


@app.route('/relatorio')
def relatorio():
    total_maquinas = len(frota)
    em_alerta = sum(1 for m in frota if m['status'] == "Manutenção Requerida")
    operacionais = total_maquinas - em_alerta
    
    # Cálculo de porcentagem de disponibilidade da frota
    disponibilidade = (operacionais / total_maquinas * 100) if total_maquinas > 0 else 0
    
    return render_template('relatorio.html', 
                           total=total_maquinas, 
                           alerta=em_alerta, 
                           operacionais=operacionais,
                           disponibilidade=round(disponibilidade, 1))

if __name__ == '__main__':
    app.run(debug=True)