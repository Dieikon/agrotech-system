import sqlite3
import random

def simular_telemetria(id_maquina):
    conn = sqlite3.connect('database.db')
    
    # Gerando dados falsos realistas para uma Colhedora de Cana
    oleo_motor = round(random.uniform(35.0, 100.0), 1)
    oleo_hidraulico = round(random.uniform(80.0, 98.0), 1)
    oleo_diesel = round(random.uniform(12.0, 95.0), 1)
    temp_motor = round(random.uniform(85.0, 105.0), 1) # Acima de 100 vai ficar vermelho na tela
    status = random.choice(['Colhendo Cana', 'Motor Ocioso', 'Em Manutenção'])
    
    # Se estiver ocioso ou em manutenção, não colhe nada.
    toneladas_hora = round(random.uniform(60.0, 90.0), 1) if status == 'Colhendo Cana' else 0.0

    # CORRIGIDO: Adicionado o 7º '?' para o oleo_diesel
    conn.execute('''
        INSERT INTO telemetria (maquina_id, nivel_oleo_motor, nivel_oleo_hidraulico, oleo_diesel, temp_motor, status_operacao, toneladas_hora)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id_maquina, oleo_motor, oleo_hidraulico, oleo_diesel, temp_motor, status, toneladas_hora))
    
    conn.commit()
    conn.close()
    print(f"Dados injetados com sucesso para a máquina {id_maquina}! Status: {status} | Diesel: {oleo_diesel}%")

# Simulando dados para a máquina ID 1 (Que deve ser a Colhedora CH570)
simular_telemetria(1)