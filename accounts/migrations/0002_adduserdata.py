# Generated by Django 3.2.4 on 2021-07-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adduserdata',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('addmission_no', models.IntegerField()),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('image', models.ImageField(default='', upload_to='pyimage')),
            ],
        ),
    ]