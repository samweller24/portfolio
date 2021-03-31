# Generated by Django 3.0.6 on 2021-02-13 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]