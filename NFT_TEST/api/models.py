from django.db import models


class Token(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='Уникальный номер'
    )
    unique_hash = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Уникальный хэш'
    )
    tx_hash = models.TextField(
        unique=True,
        verbose_name='Хэш транзакции создания токена'
    )
    media_url = models.TextField(
        verbose_name='URL с произвольным изображением'
    )
    owner = models.TextField(
        verbose_name='Адрес пользователя в сети Ethereum'
    )

    def __str__(self):
        return self.id
