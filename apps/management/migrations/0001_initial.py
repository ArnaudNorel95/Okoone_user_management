# Generated by Django 4.2.5 on 2023-09-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(db_column='ArtistId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=120)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(db_column='EmployeeId', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='FirstName', max_length=40)),
                ('last_name', models.CharField(db_column='LastName', max_length=20)),
                ('title', models.CharField(db_column='Title', default='', max_length=30)),
                ('birth_date', models.DateTimeField(db_column='BirthDate')),
                ('hire_date', models.DateTimeField(db_column='HireDate')),
                ('address', models.CharField(db_column='Address', default='', max_length=70)),
                ('city', models.CharField(db_column='City', default='', max_length=40)),
                ('state', models.CharField(db_column='State', default='', max_length=40)),
                ('country', models.CharField(db_column='Country', default='', max_length=40)),
                ('postal_code', models.CharField(db_column='PostalCode', default='', max_length=10)),
                ('phone', models.CharField(db_column='Phone', default='', max_length=24)),
                ('fax', models.CharField(db_column='Fax', default='', max_length=24)),
                ('email', models.CharField(db_column='Email', max_length=60)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(db_column='CustomerId', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='FirstName', max_length=40)),
                ('last_name', models.CharField(db_column='LastName', max_length=20)),
                ('company', models.CharField(db_column='Company', default='', max_length=80)),
                ('address', models.CharField(db_column='Address', default='', max_length=70)),
                ('city', models.CharField(db_column='City', default='', max_length=40)),
                ('state', models.CharField(db_column='State', default='', max_length=40)),
                ('country', models.CharField(db_column='Country', default='', max_length=40)),
                ('postal_code', models.CharField(db_column='PostalCode', default='', max_length=10)),
                ('phone', models.CharField(db_column='Phone', default='', max_length=24)),
                ('fax', models.CharField(db_column='Fax', default='', max_length=24)),
                ('email', models.CharField(db_column='Email', max_length=60)),
                ('support_employee', models.ForeignKey(db_column='SupportRepId', on_delete=django.db.models.deletion.DO_NOTHING, to='management.employees')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
