# Generated by Django 5.1.2 on 2024-10-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskmatrix',
            name='mitigation',
            field=models.CharField(max_length=100),
        ),
    ]
