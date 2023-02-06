import requests
import pytest

id = 2


@pytest.mark.django_db
def test():

    response = requests.get(url=f'http://127.0.0.1:8000/api/sensor/{id}')
    assert response.status_code == 200
    assert response.json()['id'] == id

if __name__ == '__main__':
    test()