# Generated by Django 3.1.3 on 2020-11-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={},
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
