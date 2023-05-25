from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from ..models import Carro

class CarroTestCase(TestCase):

    def setUp(self):
        pass

    def test_criar_carro_basico(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=13000,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
        except:
            self.fail("Exception was not expected.")
    
    def test_criar_carro_nome_none(self):
        try:
            Carro.objects.create(
                nome=None,
                marca="Fiat",
                ano=2020,
                km=13000,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass

    def test_criar_carro_marca_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca=None,
                ano=2020,
                km=13000,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass
        
    def test_criar_carro_ano_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=None,
                km=13000,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass

    def test_criar_carro_km_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=None,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass
    
    def test_criar_carro_estado_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=13000,
                estado=None,
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass
        
    def test_criar_carro_valor_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=13000,
                estado="SP",
                valor=None,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except IntegrityError:
            pass
        
    def test_criar_carro_foto_none(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=13000,
                estado="SP",
                valor=30000,
                foto=None
            )
            self.assertTrue(False)
        except IntegrityError:
            pass
    
    def test_criar_carro_ano_string(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano="",
                km=13000,
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except ValueError:
            pass
    
    def test_criar_carro_km_string(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km="",
                estado="SP",
                valor=30000,
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except ValueError:
            pass
    
    def test_criar_carro_valor_string(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=2020,
                km=1300,
                estado="SP",
                valor="",
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except ValidationError:
            pass
    
    def test_criar_carro_ano_alto(self):
        try:
            Carro.objects.create(
                nome="Uno",
                marca="Fiat",
                ano=19999999,
                km=1300,
                estado="SP",
                valor="",
                foto="https://images.prd.kavak.io/eyJidWNrZXQiOiJrYXZhay1pbWFnZXMiLCJrZXkiOiJpbWFnZXMvMjQ3NTkwL0VYVEVSSU9SLWZyb250U2lkZVBpbG90TmVhci0xNjgzNzUzMDk1MTM5LmpwZWciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjU0MCwiaGVpZ2h0IjozMTB9fX0="
            )
            self.fail("Exception was expected.")
        except ValidationError:
            pass