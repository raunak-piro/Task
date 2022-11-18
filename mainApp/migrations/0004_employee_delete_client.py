# Generated by Django 4.1.2 on 2022-11-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='client',
        ),
    ]
