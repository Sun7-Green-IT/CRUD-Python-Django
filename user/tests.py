from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer
from datetime import date

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(firstname="", lastname="", birthday="", email="", role_id=""):
        if firstname != "" and lastname != "" and birthday != "" and email != "" and role_id != "":
            User.objects.create(firstname=firstname, lastname=lastname,
                                birthday=birthday, email=email, role_id=role_id)

    def setUp(self):
        # add test data
        self.create_user('Arri', 'Gelletly', 'agelletly0@skyrock.com',
                         date.today(), '0cac83fb-ea03-42ec-92f7-fd372dd76ced')
        self.create_user('Arri', 'Gelletly', 'agelletly0@skyrock.com',
                         date.today(), '0cac83fb-ea03-42ec-92f7-fd372dd76eed')
        self.create_user('Arri', 'Gelletly', 'agelletly0@skyrock.com',
                         date.today(), '0cac83fb-ea03-42ec-92f7-fd372dd76ded')
        self.create_user('Arri', 'Gelletly', 'agelletly0@skyrock.com',
                         date.today(), '0cac83fb-ea03-42ec-92f7-fd372dd76ged')


class GetAllUserTest(BaseViewTest):

    def test_get_all_users(self):
        """
        This test ensures that all user added in the setUp method
        exist when we make a GET request to the user/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("user-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
