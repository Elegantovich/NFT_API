# Generated by Django 3.2.12 on 2022-03-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_token_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='media_url',
            field=models.TextField(default=1, max_length=20, unique=True, verbose_name='URL с произвольным изображением'),
            preserve_default=False,
        ),
    ]
