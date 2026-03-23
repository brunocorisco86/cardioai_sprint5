import json
import time
from datetime import datetime
import os

# Simulação de Banco de Dados Relacional (Simulando clinical_records)
# Em produção, usaríamos sqlalchemy com a DATABASE_URL
DB_SIMULADO = [
    {"id": 1, "userId": 10, "pa_sis": 120, "pa_dia": 80, "fc": 70, "created_at": "2026-03-22 10:00:00"},
    {"id": 2, "userId": 10, "pa_sis": 145, "pa_dia": 95, "fc": 88, "created_at": "2026-03-22 11:00:00"},
    {"id": 3, "userId": 11, "pa_sis": 130, "pa_dia": 85, "fc": 75, "created_at": "2026-03-22 10:30:00"},
    {"id": 4, "userId": 10, "pa_sis": 150, "pa_dia": 100, "fc": 95, "created_at": "2026-03-22 12:00:00"},
]

LOG_FILE = "python/execution_logs.json"

def monitorar_sinais_vitais():
    print("Iniciando Monitoramento RPA - CardioIA")
    
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)

    for registro in DB_SIMULADO:
        print(f"Processando registro {registro['id']} do usuário {registro['userId']}...")
        
        # Lógica de IA/Regras de Negócio para identificar anomalias
        anomalia = False
        mensagem = "Sinais normais"
        
        if registro['pa_sis'] > 140 or registro['pa_dia'] > 90:
            anomalia = True
            mensagem = "ALERTA: Hipertensão detectada!"
        elif registro['fc'] > 100:
            anomalia = True
            mensagem = "ALERTA: Taquicardia detectada!"
            
        # Registrar no log (Não-relacional)
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "registro_id": registro['id'],
            "usuario_id": registro['userId'],
            "status": "ANOMALIA" if anomalia else "OK",
            "mensagem": mensagem,
            "dados": registro
        }
        
        logs.append(log_entry)
        
        if anomalia:
            print(f"!!! {mensagem} para usuário {registro['userId']}")
            
    # Salvar logs no formato JSON (Não-relacional)
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=4, ensure_all_ascii=False)
        
    print(f"Monitoramento finalizado. {len(logs)} logs registrados em {LOG_FILE}")

if __name__ == "__main__":
    monitorar_sinais_vitais()
