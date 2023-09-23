from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customers, Employees, Artists
from django.contrib.auth import hashers
from datetime import datetime
# Create your tests here.

class CustomerModelTest(TestCase):
    def test_user_creation(self):
        """
            Ensure we can create a new Customer object in Database.
        """
        employee = Employees.objects.create(
            first_name  = "Adams",
            last_name   = "Andrew",
            title       = "General Manager",
            birth_date  = "1947-09-19 00:00:00",
            hire_date   = "2003-05-03 00:00:00",
            email       = "adamsandrew@yahoo.fr"
        )

        customer = Customers.objects.create(
            first_name  = "Arnaud",
            last_name   = "Norel",
            company     = "Test",
            address     = "12th 68 Nyc",
            city        = "NYC",
            state       = "NY state",
            country     = "USA",
            postal_code = "4512",
            phone       = "+3346489",
            fax         = "+3367891",
            email       = "arnaudnorel@yahoo.fr",
            support_employee = employee
        )
        self.assertEqual(customer.first_name, "Arnaud")
        self.assertEqual(customer.last_name, "Norel")
        self.assertEqual(customer.company, "Test")
        self.assertEqual(customer.address, "12th 68 Nyc")
        self.assertEqual(customer.city, "NYC")
        self.assertEqual(customer.state, "NY state")
        self.assertEqual(customer.country, "USA")
        self.assertEqual(customer.postal_code, "4512")
        self.assertEqual(customer.phone, "+3346489")
        self.assertEqual(customer.fax, "+3367891")
        self.assertEqual(customer.email, "arnaudnorel@yahoo.fr")
        self.assertEqual(customer.support_employee.last_name, "Andrew")




# class UserApiTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.sample_user_data = {
#             "username":"arnaud_norel",
#             "password":"azrtyuiop",
#             "email":"arnaudnorel95@gmail.com",
#             "company":"Natixis"
#         }
#         ## In a first time create a test user to be allowed to access Handle User View   
#         self.user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
#         login_url = reverse("token_obtain_pair")
#         response = self.client.post(login_url, {"username":"testuser", "password":"testpassword"})
#         ## Then login and get a token access
#         self.token = response.json()['access']        
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
#         self.url = reverse("apps.gitcastle:user")

#     def test_create_artist(self):
#         """
#             Ensure we can create a new User via API.
#         """
#         response = self.client.post(self.url, self.sample_user_data, format='json')
#         saved_user = User.objects.last()
#         print("ID OF THE CON : ", saved_user.pk)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 2)
#         self.assertEqual(saved_user.username, 'arnaud_norel')
#         self.assertEqual(saved_user.company, 'Natixis')
#         self.assertEqual(saved_user.email, 'arnaudnorel95@gmail.com')
#         self.assertFalse(saved_user.is_staff)
#         #Check the password is hashed in database
#         self.assertNotEqual(saved_user.password, 'azrtyuiop')
#         self.assertTrue(saved_user.check_password('azrtyuiop'))