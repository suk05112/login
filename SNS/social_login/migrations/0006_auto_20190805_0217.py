# Generated by Django 2.2.3 on 2019-08-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_login', '0005_auto_20190805_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profileimage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]