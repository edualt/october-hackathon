# Generated by Django 4.1.2 on 2022-10-11 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_remove_company_advocates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='href',
            field=models.URLField(),
        ),
    ]
