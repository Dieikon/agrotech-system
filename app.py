from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Simulando uma frota de máquinas
    frota = [
        {"modelo": "Colhedora CH570", "status": "Operacional", "horas": 480},
        {"modelo": "Trator 8R", "status": "Manutenção Requerida", "horas": 610},
        {"modelo": "Pulverizador M4040", "status": "Operacional", "horas": 150}
    ]
    return render_template('index.html', maquinas=frota)

if __name__ == '__main__':
    app.run(debug=True)