# Generated by Django 4.0 on 2022-01-18 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_modified_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ('-created_date',), 'verbose_name': '简历', 'verbose_name_plural': '简历列表'},
        ),
    ]