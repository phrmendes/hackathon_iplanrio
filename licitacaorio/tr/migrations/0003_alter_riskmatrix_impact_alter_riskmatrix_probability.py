# Generated by Django 5.1.2 on 2024-10-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr', '0002_alter_riskmatrix_mitigation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskmatrix',
            name='impact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='riskmatrix',
            name='probability',
            field=models.IntegerField(),
        ),
    ]
