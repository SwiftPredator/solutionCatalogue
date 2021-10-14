# Generated by Django 3.2.7 on 2021-10-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20211013_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='protocols',
            field=models.CharField(help_text='Schnittstellen und/oder Protokolle, die von der Lösung unterstützt werden', max_length=1000, verbose_name='Protokolle/Schnittstellen'),
        ),
    ]
