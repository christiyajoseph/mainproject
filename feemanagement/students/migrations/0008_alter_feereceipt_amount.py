# Generated by Django 4.2.4 on 2023-08-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_feereceipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feereceipt',
            name='amount',
            field=models.CharField(max_length=250),
        ),
    ]
