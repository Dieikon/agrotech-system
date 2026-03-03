# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Simulando dados reais da colhedora John Deere
    dados = {
        "maquina": "Colhedora CH570",
        "status": "Operacional",
        "horas_uso": 480
    }
    # Enviamos a variável 'dados' para dentro do HTML
    return render_template('index.html', info=dados)

if __name__ == '__main__':
    app.run(debug=True)