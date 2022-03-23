# Generated by Django 4.0.3 on 2022-03-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
