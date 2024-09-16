from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(
        'Цена', max_digits=10, decimal_places=2,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-price',)

    def __str__(self):
        return self.name
