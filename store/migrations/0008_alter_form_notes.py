# Generated by Django 4.0.2 on 2022-03-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_form_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='notes',
            field=models.CharField(default='No Comments', max_length=200, null=True),
        ),
    ]
