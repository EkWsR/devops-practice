import pytest
from app import app  # Importa la aplicación Flask desde app.py

# Configura el cliente de prueba de Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Habilita el modo de pruebas
    with app.test_client() as client:
        yield client  # Proporciona el cliente para las pruebas

def test_suma(client):
    # Enviar solicitud POST al endpoint /suma
    response = client.post('/suma', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5

    response = client.post('/suma', json={'a': 0, 'b': 0})
    assert response.status_code == 200
    assert response.json['result'] == 0

def test_resta(client):
    # Enviar solicitud POST al endpoint /resta
    response = client.post('/resta', json={'a': 6, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 3

    response = client.post('/resta', json={'a': 0, 'b': 0})
    assert response.status_code == 200
    assert response.json['result'] == 0