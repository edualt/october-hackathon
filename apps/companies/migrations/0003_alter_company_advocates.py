# Generated by Django 4.1.2 on 2022-10-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0002_advocate_company'),
        ('companies', '0002_alter_company_advocates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='advocates',
            field=models.ManyToManyField(related_name='advocate_id', to='advocates.advocate'),
        ),
    ]