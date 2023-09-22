from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name
