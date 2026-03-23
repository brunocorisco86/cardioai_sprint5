import pytest
from python.rpa_monitor import monitorar_sinais_vitais
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_mysql():
    with patch('python.rpa_monitor.get_mysql_connection') as mock:
        yield mock

@pytest.fixture
def mock_mongo():
    with patch('python.rpa_monitor.get_mongo_collection') as mock:
        yield mock

def test_monitorar_sinais_vitais_normal(mock_mysql, mock_mongo):
    # Setup mock MySQL
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_mysql.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simular um registro normal
    mock_cursor.fetchall.return_value = [{
        'id': 1,
        'userId': 10,
        'pressaoSistolica': 120,
        'pressaoDiastolica': 80,
        'frequenciaCardiaca': 70,
        'status': 'normal',
        'createdAt': '2026-03-22 10:00:00'
    }]

    # Setup mock Mongo
    mock_collection = MagicMock()
    mock_mongo.return_value = mock_collection

    monitorar_sinais_vitais()

    # Verificar se inseriu no mongo
    assert mock_collection.insert_one.called
    # Verificar se NÃO atualizou o status (já que é normal)
    assert not mock_conn.commit.called

def test_monitorar_sinais_vitais_anomalia(mock_mysql, mock_mongo):
    # Setup mock MySQL
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_mysql.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simular um registro com hipertensão
    mock_cursor.fetchall.return_value = [{
        'id': 2,
        'userId': 11,
        'pressaoSistolica': 150,
        'pressaoDiastolica': 100,
        'frequenciaCardiaca': 80,
        'status': 'normal',
        'createdAt': '2026-03-22 11:00:00'
    }]

    # Setup mock Mongo
    mock_collection = MagicMock()
    mock_mongo.return_value = mock_collection

    monitorar_sinais_vitais()

    # Verificar se inseriu no mongo
    assert mock_collection.insert_one.called
    # Verificar se atualizou o status para alerta
    assert mock_conn.commit.called
