from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from vehicle.models import Motorcycle


class CarTestCase(APITestCase):
    """Необходимо обложить тестами один эндпоинт создания сущности и один эндпоинт отображения списка или одной \
     сущности.
    Посчитать покрытие тестами.
    pip install coverage
    coverage run --source='.' manage.py test
    coverage html
    python manage.py test vehicle.tests - команда для запуска"""

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
        """Test car create"""
        response = self.client.post('/vehicle/car/create/', {'model': self.test_model_name})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_car(self):
        """Test detail"""
        self.test_car_create()
        response = self.client.get(f'/vehicle/car/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 1, 'model': self.test_model_name, 'year': 1900, 'owner': None})

    def test_car_validation_error(self):
        """Test validation error"""
        data = {'model': 'крипта', 'year': 1900}
        response = self.client.post('/vehicle/car/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MotoTestCase(APITestCase):
    def setUp(self) -> None:
        # Подготовка данных перед каждым тестом
        self.user = User(username='max', is_staff=True)
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {"username": "max", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.moto = Motorcycle.objects.create(
            model="moto_test",
            year=2232
        )

    def test_get_list(self):
        response = self.client.get('/vehicle/moto/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_2 = self.client.post('/vehicle/moto/create/', {
            "model": "test2",
            "year": 2008
        })
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'count': 1, 'next': None, 'previous': None,
                                           'results': [{'id': 1, 'model': 'moto_test', 'year': 2232, 'owner': None}]})
        self.assertEqual(Motorcycle.objects.all().count(), 2)
