# Generated by Django 5.1.3 on 2024-12-02 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('crm', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
