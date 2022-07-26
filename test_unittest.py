
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
client.headers["Content-Type"] = "multipart/form-data"



def test_read_main():
    response = client.get("/isalive")
    assert response.status_code == 200
    assert response.json() == {'message': 'is alive'}


def test_get_file():
    response = client.post('/test', data={"path": r"C:\Users\NOY-L\Pictures\Saved Pictures\Capture3.PNG"})
    print(response)
    assert response.status_code == 200
