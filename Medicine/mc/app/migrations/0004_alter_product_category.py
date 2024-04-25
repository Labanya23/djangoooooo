# Generated by Django 5.0.4 on 2024-04-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CL', 'Cold'), ('EY', 'Eye'), ('DT', 'Dehydration'), ('HT', 'Heatstock'), ('SA', 'Seasonal allergies'), ('TP', 'Typhoid'), ('OT', 'Other')], max_length=2),
        ),
    ]
