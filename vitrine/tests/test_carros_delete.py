from django.test import TestCase, Client
from ..models import Carro
from django.contrib.auth.models import User

class CarrosPutDeleteCase(TestCase):
    
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
        carro_id = str(self.c.post('/carros/', data=self.test_carro, headers={"authorization": f"Bearer {self.token}"}).json()['id'])

        self.response = self.c.delete(f'/carros/{carro_id}/')
        self.auth_response = self.c.delete(f'/carros/{carro_id}/', headers={"authorization": f"Bearer {self.token}"})
        self.auth_response2 = self.c.delete(f'/carros/42/', headers={"authorization": f"Bearer {self.token}"})
        self.auth_response_no_bearer = self.c.delete(f'/carros/{carro_id}', headers={"authorization": f"{self.token}"})
        self.auth_response_invalid = self.c.delete(f'/carros/{carro_id}', headers={"authorization": f"Bearer asfjas3"})

    # Testing unauthenticated
    def test_delete_nao_autenticado(self):
        self.assertEqual(401, self.response.status_code)
    
    def test_delete_token_invalido(self):
        self.assertEqual(301, self.auth_response_invalid.status_code)
    
    def test_post_sem_bearer_retorna_401(self):
        self.assertEqual(301, self.auth_response_no_bearer.status_code)

    # Testing authenticated
    def test_delete_carro_com_autenticacao_retorna_201(self):
        self.assertEqual(204, self.auth_response.status_code)