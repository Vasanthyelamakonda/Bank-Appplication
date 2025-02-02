# Generated by Django 5.1.4 on 2025-01-10 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0007_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_period', models.PositiveIntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.customer')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.loan')),
            ],
        ),
    ]
