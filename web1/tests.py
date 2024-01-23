from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class TestHelloWord(TestCase):
    def setUp(self) -> None:
        self.url = reverse('hello_word')

    def test_gets(self):
        response = self.client.get(self.url)

        assert response.status_code == 200
        assert response.json()['message'] == 'hello_word'
