# Generated by Django 4.0 on 2022-01-05 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_resume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': '职位', 'verbose_name_plural': '职位列表'},
        ),
    ]