# Generated by Django 4.1.2 on 2022-10-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_company_href'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='advocates',
        ),
    ]