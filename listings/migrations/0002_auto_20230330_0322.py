# Generated by Django 3.1.14 on 2023-03-30 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-name',), 'verbose_name_plural': 'categories'},
        ),
    ]