import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_dolar_observado():
    response = client.get("/indicadores/dolar")
    assert response.status_code == 200
    data = json.loads(response.text)
    assert "value" in data
    assert isinstance(data["value"], dict)
    assert "dolar" in data["value"]
    assert isinstance(data["value"]["dolar"], dict)
    assert "valor" in data["value"]["dolar"]
    assert isinstance(data["value"]["dolar"]["valor"], float)