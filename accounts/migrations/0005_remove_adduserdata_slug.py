# Generated by Django 3.2.4 on 2021-07-03 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_adduserdata_admission_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adduserdata',
            name='slug',
        ),
    ]
