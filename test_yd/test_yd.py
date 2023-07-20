import unittest
from unittest import TestCase
import requests


class TestYandexDisk(TestCase):

    def setUp(self):
        self.token = ''  # записываем здесь свой токен
        self.folder_name = ''  # название папки
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def test_create_folder(self):
        params = {'path': f'/{self.folder_name}'}
        response = requests.put(f'{self.url}/', headers=self.headers, params=params)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()