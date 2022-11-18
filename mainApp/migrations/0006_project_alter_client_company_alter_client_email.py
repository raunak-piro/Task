# Generated by Django 4.1.2 on 2022-11-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('project_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]