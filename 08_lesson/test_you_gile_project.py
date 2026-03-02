import requests

BASE_URL = "https://yougile.com/api-v2/"
TOKEN = "мой токен"
headers = {"Authorization": f"Bearer {TOKEN}"}


def test_create_project_positive():
    payload = {"title": "ГосУслуги"}
    response = requests.post(BASE_URL + "projects", json=payload, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative():
    payload = {"title": 123}
    response = requests.post(BASE_URL + "projects", json=payload, headers=headers)
    assert response.status_code == 400
    assert "Bad Request" in response.json()["error"]

def test_update_project_positive():
    payload_1 = {"title": "ГосУслуги_1"}
    response_post = requests.post(BASE_URL + "projects", json=payload_1, headers=headers)
    project_id = response_post.json()["id"]

    payload_2 = {"title": "ГосУслуги_2"}
    response_update = requests.put(BASE_URL + "projects/" + f"{project_id}", json=payload_2, headers=headers)

    assert response_update.status_code == 200
    assert "id" in response_update.json()

def test_update_project_negative():
    payload_2 = {"title": "ГосУслуги_2"}
    project_id ="12312412421"
    response_update = requests.put(BASE_URL + "projects/" + f"{project_id}", json=payload_2, headers=headers)

    assert response_update.status_code == 404
    assert "Not Found" in response_update.json()["error"]

def test_get_project_positive():
    payload = {"title": "ГосУслуги"}
    response = requests.post(BASE_URL + "projects", json=payload, headers=headers)

    response_get = requests.get(BASE_URL + "projects", headers=headers)
    assert len(response_get.json()) > 0
    assert response.status_code == 201


def test_get_project_negative():
    payload = {"title": "ГосУслуги"}
    requests.post(BASE_URL + "projects", json=payload, headers=headers)

    response_get = requests.get(BASE_URL + "projects/" + 'abc', headers=headers)
    assert response_get.status_code == 404
    assert "Not Found" in response_get.json()["error"]
