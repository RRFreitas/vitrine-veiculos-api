
from django.test import TestCase, Client
from ..models import Carro
from django.contrib.auth.models import User

class CarrosPostTestCase(TestCase):
    
    def setUp(self):
        # Registering fake user for testting
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.c = Client()
        response = self.c.post("/token/", {"username": "testuser", "password": "12345"})
        self.token = response.json()['access']

        # Fake cars for test
        self.test_carro = {
            "nome":"Uno",
            "marca":"Fiat",
            "ano":2020,
            "km":1300,
            "estado":"SP",
            "valor":30000,
            "foto":"https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
        }
        self.test_carro2 = {
            "nome":"Uno",
            "marca":"Fiat",
            "ano":2020,
            "km":1300,
            "valor":30000,
        }
        self.test_carro3 = {}

        self.response = self.c.post('/carros/', data=self.test_carro)
        self.auth_response = self.c.post('/carros/', data=self.test_carro, headers={"authorization": f"Bearer {self.token}"})
        self.auth_response2 = self.c.post('/carros/', data=self.test_carro2, headers={"authorization": f"Bearer {self.token}"})
        self.auth_response3 = self.c.post('/carros/', data=self.test_carro3, headers={"authorization": f"Bearer {self.token}"})
        self.auth_response_no_bearer = self.c.post('/carros/', data=self.test_carro, headers={"authorization": f"{self.token}"})
        self.auth_response_invalid = self.c.post('/carros/', data=self.test_carro, headers={"authorization": f"Bearer asfjas3"})

    # Testing unauthenticated
    def test_post_nao_autenticado(self):
        self.assertEqual(401, self.response.status_code)
    
    def test_post_token_invalido(self):
        self.assertEqual(401, self.auth_response_invalid.status_code)

    def test_post_sem_bearer_retorna_401(self):
        self.assertEqual(401, self.auth_response_no_bearer.status_code)

    # Testing authenticated
    def test_post_carro_com_autenticacao_retorna_201(self):
        self.assertEqual(201, self.auth_response.status_code)

    def test_post_carro_com_autenticacao_retorna_json(self):
        self.assertEqual('application/json', self.auth_response.headers['Content-Type'])
    
    def test_post_carro_com_autenticacao_retorna_carro(self):
        response = dict(self.auth_response.json())
        response.pop('id')
        response['valor'] = int(float(response['valor']))
        self.assertEqual(self.test_carro, response)

    def test_post_carro_faltando_campos_retorna_400(self):
        self.assertEqual(400, self.auth_response2.status_code)
    
    def test_post_carro_vazio_retorna_400(self):
        self.assertEqual(400, self.auth_response3.status_code)