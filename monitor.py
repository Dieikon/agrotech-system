# monitor.py

def verificar_status_maquina(nome_maquina, horas_uso):
    print(f"--- Analisando {nome_maquina} ---")
    if horas_uso >= 500:
        return "⚠️ ALERTA: Necessário manutenção preventiva (Troca de Óleo)."
    else:
        return "✅ STATUS: Máquina operando em condições ideais."

# Simulando dados de uma colhedora John Deere
maquina = "Colhedora CH570"
horas = 550  # Altere este valor para testar a lógica

resultado = verificar_status_maquina(maquina, horas)
print(resultado)