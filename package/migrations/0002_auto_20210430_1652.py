# Generated by Django 3.2 on 2021-04-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=150)),
                ('periodicity', models.CharField(max_length=150)),
                ('disk_space', models.CharField(max_length=150)),
                ('bandwidth', models.CharField(max_length=150)),
                ('discount', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name_plural': 'Packages'},
        ),
    ]
