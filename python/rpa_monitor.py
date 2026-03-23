import json
import time
from datetime import datetime
import os
import mysql.connector
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

# Configurações de Banco de Dados Relacional (MySQL)
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'cardioia'),
    'port': int(os.getenv('DB_PORT', 3306))
}

# Configuração de Banco de Dados Não-Relacional (MongoDB)
MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'cardioia_logs')

def get_mysql_connection():
    try:
        # Tentar extrair do DATABASE_URL se existir
        db_url = os.getenv('DATABASE_URL')
        if db_url and db_url.startswith('mysql://'):
            url = urlparse(db_url)
            return mysql.connector.connect(
                user=url.username,
                password=url.password,
                host=url.hostname,
                port=url.port or 3306,
                database=url.path.lstrip('/')
            )

        return mysql.connector.connect(**DB_CONFIG)
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def get_mongo_collection():
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        return db['execution_logs']
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

def monitorar_sinais_vitais():
    print("Iniciando Monitoramento RPA - CardioIA")
    
    conn = get_mysql_connection()
    if not conn:
        print("Falha na conexão com MySQL. Abortando.")
        return

    mongo_collection = get_mongo_collection()
    if mongo_collection is None:
        print("Falha na conexão com MongoDB. Logs serão apenas impressos.")

    cursor = conn.cursor(dictionary=True)

    # Busca registros clínicos recentes (exemplo: últimos 100)
    cursor.execute("SELECT * FROM clinical_records ORDER BY createdAt DESC LIMIT 100")
    registros = cursor.fetchall()

    for registro in registros:
        print(f"Processando registro {registro['id']} do usuário {registro['userId']}...")
        
        # Lógica de IA/Regras de Negócio para identificar anomalias
        anomalia = False
        mensagem = "Sinais normais"
        
        # Regras simples de triagem (IA Simbólica/Heurística)
        if registro['pressaoSistolica'] > 140 or registro['pressaoDiastolica'] > 90:
            anomalia = True
            mensagem = "ALERTA: Hipertensão detectada!"
        elif registro['frequenciaCardiaca'] > 100:
            anomalia = True
            mensagem = "ALERTA: Taquicardia detectada!"
        elif registro['frequenciaCardiaca'] < 50:
            anomalia = True
            mensagem = "ALERTA: Bradicardia detectada!"
            
        # Registrar no log (Não-relacional - MongoDB)
        log_entry = {
            "timestamp": datetime.now(),
            "registro_id": registro['id'],
            "usuario_id": registro['userId'],
            "status": "ANOMALIA" if anomalia else "OK",
            "mensagem": mensagem,
            "dados": {
                "pa_sis": registro['pressaoSistolica'],
                "pa_dia": registro['pressaoDiastolica'],
                "fc": registro['frequenciaCardiaca'],
                "created_at": registro['createdAt'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(registro['createdAt'], datetime) else registro['createdAt']
            }
        }
        
        if mongo_collection is not None:
            mongo_collection.insert_one(log_entry)
        
        # Atualizar o status do registro no banco relacional se necessário
        if anomalia and registro['status'] == 'normal':
            with conn.cursor() as update_cursor:
                update_cursor.execute(
                    "UPDATE clinical_records SET status = %s WHERE id = %s",
                    ("alerta", registro['id'])
                )
                conn.commit()
            print(f"!!! {mensagem} para usuário {registro['userId']} - Status atualizado para 'alerta'")
            
    cursor.close()
    conn.close()
    print(f"Monitoramento finalizado. {len(registros)} registros processados.")

if __name__ == "__main__":
    monitorar_sinais_vitais()
