# Generated by Django 4.0.5 on 2022-06-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhaar_Number', models.BigIntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=20)),
                ('Mobile_Number', models.BigIntegerField()),
                ('Dose', models.IntegerField()),
                ('Vaccine_Name', models.CharField(max_length=20)),
            ],
        ),
    ]