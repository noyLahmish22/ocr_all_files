from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/isalive")
    assert response.status_code == 200
    assert response.json() == {'message': 'is alive'}


def test_get_file():
    response = client.post('/test',
                           params={"path": r"C:\Users\NOY-L\Pictures\Saved Pictures\Capture3.PNG", "language": "heb"})
    assert response.status_code == 200
    assert response.json()["data"] != ""
