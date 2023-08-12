import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        yield app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "pode o filho",
            "last_name": "de uma enfermeira",
            "cpf": "818.806.010-01",
            "email": "lupedelupe@gmail.com",
            "birth_date": "2020-10-19"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "pode o filho",
            "last_name": "de uma enfermeira",
            "cpf": "818.806.010-04",
            "email": "lupedelupe@gmail.com",
            "birth_date": "2020-10-19"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data
