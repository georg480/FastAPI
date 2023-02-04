import pytest

from main import add, devide

def test_add():
    result = add(2, 3)
    assert result == 5

def test_devide():
    result = devide(8, 2)
    assert result == 4
    with pytest.raises(ZeroDivisionError):
        10/0
    ##
#client = TestClient(app)


#def test_root():
#    response = client.get("/")
 #   assert response.status_code == 200
 #   assert response.json()["message"] == "Hello World"


#def test_say_hello():
 #   response = client.get("/hello/User")
  #  result = response.json()
   # assert response.status_code == 200
   # assert result["message"] == "Hello User"
