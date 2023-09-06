# Generated by Django 4.2.4 on 2023-09-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='Medium', max_length=5),
        ),
    ]
