from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class CarTestCase(APITestCase):
    """Необходимо обложить тестами один эндпоинт создания сущности и один эндпоинт отображения списка или одной \
     сущности.
    Посчитать покрытие тестами."""
    def setUp(self) -> None:
        # Подготовка данных перед каждым тестом
        self.user = User(username='max', is_staff=True)
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {"username": "max", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'audi a100'

    def test_car_create(self):
        response = self.client.post('/vehicle/car/create/', {'model': self.test_model_name})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_car(self):
        self.test_car_create()
        response = self.client.get(f'/vehicle/car/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 1, 'model': self.test_model_name, 'year': 1900, 'owner': None})
