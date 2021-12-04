from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import models
from http import HTTPStatus


class UserTestCase(TestCase):
    def setUp(self):
        self.c = Client()


    def test_page_is_ok_register(self):
        response = self.c.get('/register', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)






