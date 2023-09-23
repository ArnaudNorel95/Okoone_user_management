from django.db import models

# Create your models here.
class Employees(models.Model):
    '''
        Informations about the table employees
        Notice that CamelCase is exceptionnaly used for matching with sample.db
    '''
    id          = models.AutoField(primary_key=True, db_column="EmployeeId")
    first_name  = models.CharField(max_length=40, null=False, db_column="FirstName")
    last_name   = models.CharField(max_length=20, null=False, db_column="LastName")
    title       = models.CharField(max_length=30, default="", db_column="Title")
    birth_date  = models.DateTimeField(db_column="BirthDate")
    hire_date   = models.DateTimeField(db_column="HireDate")
    address     = models.CharField(max_length=70, default="", db_column="Address")
    city        = models.CharField(max_length=40, default="", db_column="City")
    state       = models.CharField(max_length=40, default="", db_column="State")
    country     = models.CharField(max_length=40, default="", db_column="Country")
    postal_code = models.CharField(max_length=10, default="", db_column="PostalCode")
    phone       = models.CharField(max_length=24, default="", db_column="Phone")
    fax         = models.CharField(max_length=24, default="", db_column="Fax")
    email       = models.CharField(max_length=60, null=False, db_column="Email")

    def __str__(self):
        return self.LastName

class Customers(models.Model):
    '''
        Informations about the table customers
        Notice that CamelCase is exceptionnaly used for matching with sample.db
    '''
    id          = models.AutoField(primary_key=True, db_column='CustomerId')
    first_name  = models.CharField(max_length=40, null=False, db_column="FirstName")
    last_name   = models.CharField(max_length=20, null=False, db_column="LastName")
    company     = models.CharField(max_length=80, default="", db_column="Company")
    address     = models.CharField(max_length=70, default="", db_column="Address")
    city        = models.CharField(max_length=40, default="", db_column="City")
    state       = models.CharField(max_length=40, default="", db_column="State")
    country     = models.CharField(max_length=40, default="", db_column="Country")
    postal_code = models.CharField(max_length=10, default="", db_column="PostalCode")
    phone       = models.CharField(max_length=24, default="", db_column="Phone")
    fax         = models.CharField(max_length=24, default="", db_column="Fax")
    email       = models.CharField(max_length=60, null=False, db_column="Email")
    support_employee    = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, db_column='SupportRepId')

    def __str__(self):
        return self.LastName
    
class Artists(models.Model):
    '''
        Informations about the table artists
        Notice that CamelCase is exceptionnaly used for matching with sample.db
    '''
    id          = models.AutoField(primary_key=True, db_column='ArtistId')
    name        = models.CharField(max_length=120, null=False, db_column="Name")

    def __str__(self):
        return self.name
    
