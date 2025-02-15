# Generated by Django 5.1.2 on 2024-10-22 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
                ('justification', models.TextField()),
                ('description', models.TextField()),
                ('service_location', models.CharField(max_length=100)),
                ('scheduled_date', models.DateField()),
                ('adm_process', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tr', to='etp.admprocess')),
            ],
        ),
        migrations.CreateModel(
            name='RiskMatrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('risk', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(blank=True, max_length=100)),
                ('probability', models.CharField(max_length=100)),
                ('impact', models.CharField(max_length=100)),
                ('strategy', models.CharField(max_length=100)),
                ('mitigation', models.TextField()),
                ('in_charge', models.CharField(max_length=100)),
                ('tr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='risk_matrix', to='tr.tr')),
            ],
        ),
    ]
