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
            Ensure Customer is working - Database Side.
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

        self.url = reverse("customers-list")    

    def test_create_customer(self):
        """
            Ensure we can't create a new Customer according to the ReadOnly Viewset- API side
        """
        response = self.client.post(self.url, data=self.sample_customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Customers.objects.count(), 0)