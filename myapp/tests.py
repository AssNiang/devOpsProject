# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Visit
import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class VisitCountTestCase(TestCase):

    def test_visit_count(self):
        # Créez un objet de comptage des visites dans la base de données
        visit = Visit.objects.create(count=0)

        # Effectuez une requête GET vers le endpoint visit_count
        response = self.client.get(reverse('visit-count'))

        # Vérifiez que la réponse a un code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Analysez la réponse JSON
        data = json.loads(response.content)

        # Vérifiez que le champ 'count' dans la réponse est égal à 1 (augmenté de 1)
        self.assertEqual(data['count'], 1)

        # Vérifiez que l'objet de comptage des visites dans la base de données a également été mis à jour
        updated_visit = Visit.objects.get(pk=visit.pk)
        self.assertEqual(updated_visit.count, 1)


class AddUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_user(self):
        data = {'username': 'utilisateur4',
                'email': 'utilisateur2@example.com',
                'first_name': 'Prénom2',
                'last_name': 'Nom2'}
        response = self.client.post(reverse('add-api'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_user_bad_request(self):
        data = {'username': '',
                'email': 'utilisateur2@example.com',
                'first_name': 'Prénom2',
                'last_name': 'Nom2'}  # Données invalides
        response = self.client.post(reverse('add-api'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
