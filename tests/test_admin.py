import json

from app import create_app

app = create_app()

def test_admin_home():
    # response = app.test_client().get('http://127.0.0.1:5000/admin')
    response = app.test_client().get('admin/')
    # print()
    # print('++++++++++++++++++++++++++++++')
    # print(response.data.decode('utf-8'))
    # print('++++++++++++++++++++++++++++++')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert response.status_code == 200
