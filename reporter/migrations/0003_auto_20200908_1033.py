# Generated by Django 3.1.1 on 2020-09-08 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userinfo_registered_on'),
        ('reporter', '0002_report_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.userinfo'),
        ),
    ]
