# Generated by Django 3.1.7 on 2021-05-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210503_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='rating',
            field=models.IntegerField(max_length=5),
        ),
    ]
