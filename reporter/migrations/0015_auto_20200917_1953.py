# Generated by Django 3.1.1 on 2020-09-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0014_auto_20200917_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=56, verbose_name='Subject'),
        ),
    ]
