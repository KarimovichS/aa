from django.test import TestCase
from django.urls import reverse
from ecdsa.test_ellipticcurve import r


# Create your tests here.


class TestHome(TestCase):
    def setUp(self) -> None:
        self.url = reverse('home')
        self.response = self.client.get('home')

    def test_gets(self):
        response = self.client.get(self.url)

        assert response.status_code == 200
        # assert response.json()['title'] == 'bosh menyu'

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')


class TestAbout(TestCase):
    def setUp(self) -> None:
        self.url = reverse('about')
        self.response = self.client.get('about')

    def test_get(self):
        response = self.client.get(self.url)
        assert response.status_code == 200

    def test_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
