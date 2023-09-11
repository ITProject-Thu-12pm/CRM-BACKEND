# Generated by Django 4.2.5 on 2023-09-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_email', models.CharField(max_length=100)),
            ],
        ),
    ]
