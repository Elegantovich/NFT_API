# Generated by Django 3.2.12 on 2022-03-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_token_media_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='tx_hash',
            field=models.CharField(default=0, max_length=50, unique=True, verbose_name='Хэш транзакции создания токена'),
            preserve_default=False,
        ),
    ]
