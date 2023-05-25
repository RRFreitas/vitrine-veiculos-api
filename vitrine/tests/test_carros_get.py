from django.test import TestCase, Client
from ..models import Carro
from django.contrib.auth.models import User

class CarrosGetTestCase(TestCase):
    
    def setUp(self):
        # Registering fake user for testting
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.c = Client()
        response = self.c.post("/token/", {"username": "testuser", "password": "12345"})
        self.token = response.json()['access']

        self.response = self.c.get('/carros/')
        self.auth_response = self.c.get('/carros/', headers={"authorization": f"Bearer {self.token}"})
        self.auth_response_no_bearer = self.c.get('/carros/', headers={"authorization": f"{self.token}"})
        self.auth_response_invalid = self.c.get('/carros/', headers={"authorization": f"Bearer asfjas3"})

    # Testing authenticated
    def test_get_carros_com_autenticacao_retorna_200(self):
        self.assertEqual(200, self.auth_response.status_code)

    def test_get_carros_com_autenticacao_retorna_json(self):
        self.assertEqual('application/json', self.auth_response.headers['Content-Type'])

    # Testing unauthenticated

    def test_get_carros_sem_autenticacao_retorna_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_carros_com_autenticacao_sem_bearer_retorna_200(self):
        self.assertEqual(200, self.auth_response_no_bearer.status_code)
    
    def test_get_carros_com_autenticacao_invalida_retorna_401(self):
        self.assertEqual(401, self.auth_response_invalid.status_code)