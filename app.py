from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Criamos a lista fora da função para que ela não resete toda vez
frota = [
    {"modelo": "Colhedora CH570", "horas": 480, "status": "Operacional"},
    {"modelo": "Trator 8R", "horas": 610, "status": "Manutenção Requerida"},
    {"modelo": "Pulverizador M4040", "horas": 150, "status": "Operacional"}
]

@app.route('/')
def home():
    return render_template('index.html', maquinas=frota)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    modelo = request.form.get('modelo')
    horas = int(request.form.get('horas'))
    
    # Lógica Automática de Status
    status = "Manutenção Requerida" if horas >= 600 else "Operacional"
    
    # Adiciona na nossa lista "em memória"
    frota.append({"modelo": modelo, "horas": horas, "status": status})
    
    return redirect(url_for('home'))


# Rota para Excluir
@app.route('/excluir/<int:indice>')
def excluir(indice):
    if 0 <= indice < len(frota):
        frota.pop(indice) # Remove a máquina da lista pelo número da linha
    return redirect(url_for('home'))

# Rota para Editar (Prepara os dados para o formulário)
@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    if request.method == 'POST':
        frota[indice]['modelo'] = request.form.get('modelo')
        frota[indice]['horas'] = int(request.form.get('horas'))
        # Recalcula o status automaticamente
        frota[indice]['status'] = "Manutenção Requerida" if frota[indice]['horas'] >= 600 else "Operacional"
        return redirect(url_for('home'))
    
    # Se for GET, enviamos os dados da máquina atual para uma página de edição
    maquina = frota[indice]
    return render_template('editar.html', maquina=maquina, indice=indice)

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