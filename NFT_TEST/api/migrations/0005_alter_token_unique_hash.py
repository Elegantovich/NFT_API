# Generated by Django 3.2.12 on 2022-03-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220329_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='unique_hash',
            field=models.CharField(max_length=21, unique=True, verbose_name='Уникальный хэш'),
        ),
    ]