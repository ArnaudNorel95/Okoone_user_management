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
            Ensure Customers are working - Database Side.
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

class CustomerApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        employee = Employees.objects.create(
            first_name  = "Adams",
            last_name   = "Andrew",
            title       = "General Manager",
            birth_date  = "1947-09-19 00:00:00",
            hire_date   = "2003-05-03 00:00:00",
            email       = "adamsandrew@yahoo.fr"
        )

        customer_a = Customers.objects.create(
            first_name  = "testa",
            last_name   = "testa",
            company     = "Testa",
            address     = "12th 68 Nyc",
            city        = "NYC",
            state       = "NY state",
            country     = "USA",
            postal_code = "4512",
            phone       = "+3346489",
            fax         = "+3367891",
            email       = "testa@yahoo.fr",
            support_employee = employee
        )

        customer_b = Customers.objects.create(
            first_name  = "testb",
            last_name   = "testb",
            company     = "Testb",
            address     = "12th 68 Nyc",
            city        = "NYC",
            state       = "NY state",
            country     = "USA",
            postal_code = "4512",
            phone       = "+3346489",
            fax         = "+3367891",
            email       = "testb@yahoo.fr",
            support_employee = employee
        )

        self.sample_customer_data = {
            "first_name":"Arnaud",
            "last_name":"Norel",
            "company":"Test",
            "address":"12th 68 Nyc",
            "city":"NYC",
            "state":"NY state",
            "country":"USA",
            "postal_code":"4512",
            "phone":"+3346489",
            "fax":"+3367891",
            "email":"arnaudnorel@yahoo.fr",
            "support_employee":employee.id
        }

        self.url_list = reverse("customers-list")
        self.url_detail = reverse("customers-detail", kwargs={'pk': 1}) 


    def test_read_customers(self):
        """
            Ensure we can get Customer list - API side
        """
        response = self.client.get(self.url_list, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customers.objects.count(), 2)

        last_customer = Customers.objects.last()
        self.assertEqual(last_customer.first_name, 'testb')
        self.assertEqual(last_customer.last_name, 'testb')
        self.assertEqual(last_customer.company, 'Testb')
        self.assertEqual(last_customer.address, '12th 68 Nyc')
        self.assertEqual(last_customer.city, 'NYC')
        self.assertEqual(last_customer.state, 'NY state')
        self.assertEqual(last_customer.country, 'USA')
        self.assertEqual(last_customer.postal_code, '4512')
        self.assertEqual(last_customer.phone, '+3346489')
        self.assertEqual(last_customer.fax, '+3367891')
        self.assertEqual(last_customer.email, 'testb@yahoo.fr')
        self.assertEqual(last_customer.support_employee.last_name, 'Andrew')


    def test_read_specific_customer(self):
        """
            Ensure we can get 1 specific Customer - API side
        """
        response = self.client.get(self.url_detail, format='json')
        customer_a_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(customer_a_data['first_name'], 'testa')
        self.assertEqual(customer_a_data['last_name'], 'testa')
        self.assertEqual(customer_a_data['company'], 'Testa')
        self.assertEqual(customer_a_data['address'], '12th 68 Nyc')
        self.assertEqual(customer_a_data['city'], 'NYC')
        self.assertEqual(customer_a_data['state'], 'NY state')
        self.assertEqual(customer_a_data['country'], 'USA')
        self.assertEqual(customer_a_data['postal_code'], '4512')
        self.assertEqual(customer_a_data['phone'], '+3346489')
        self.assertEqual(customer_a_data['fax'], '+3367891')
        self.assertEqual(customer_a_data['email'], 'testa@yahoo.fr')
        self.assertEqual(customer_a_data['support_employee'], 1)        

    def test_create_customer(self):
        """
            Ensure we can't create a new Customer according to the ReadOnly Viewset- API side
            Firstly we remove the customers added in database in precedent test, to have an empty table
        """
        Customers.objects.all().delete()
        response = self.client.post(self.url_list, data=self.sample_customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Customers.objects.count(), 0)

class ArtistModelTest(TestCase):
    def test_user_creation(self):
        """
            Ensure Artists is working - Database Side.
        """
        artist = Artists.objects.create(
            name  = "50 Cent"
        )

        self.assertEqual(artist.name, "50 Cent")

class ArtistApiTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.sample_artist_data = {
            "name": "Eminem"
        }