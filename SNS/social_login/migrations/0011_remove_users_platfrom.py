# Generated by Django 2.2.3 on 2019-08-08 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_login', '0010_auto_20190809_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='platfrom',
        ),
    ]