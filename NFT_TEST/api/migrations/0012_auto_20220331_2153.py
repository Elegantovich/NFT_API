# Generated by Django 3.2.12 on 2022-03-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_token_media_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='media_url',
            new_name='mediaURL',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='unique_hash',
            new_name='uniqueHash',
        ),
        migrations.AlterField(
            model_name='token',
            name='owner',
            field=models.TextField(verbose_name='Адрес пользователя в сети Ethereum'),
        ),
    ]
