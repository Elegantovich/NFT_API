# Generated by Django 3.2.12 on 2022-03-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220331_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='media_url',
            field=models.TextField(verbose_name='URL с произвольным изображением'),
        ),
    ]