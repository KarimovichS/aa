
from django.test import TestCase
from django.urls import reverse, resolve
from ecdsa.test_ellipticcurve import r


from . import views


# Create your tests here.


class TestHome(TestCase):
    def setUp(self) -> None:
        self.url = reverse('home')
        self.url_view = reverse('about')
        self.response = self.client.get('home')

    def test_gets(self):
        response = self.client.get(self.url)

        assert response.status_code == 200
        # assert response.json()['title'] == 'bosh menyu'

    def test_template(self):
        self.assertEquals(resolve(self.url).func, views.index)

    def test_about(self):
        self.assertEquals(resolve(self.url_view).func, views.about)

    def test_view_menu(self):
        response = self.client.get(self.url)
        menu_set = response.context['menu']
        assert menu_set is not None



