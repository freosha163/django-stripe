from django.db import models


class Item(models.Model):
    """Модель продукта"""

    class ItemCurrency(models.TextChoices):
        USD = 'USD'
        Euro = 'Euro'
        
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0) # в центах
    currency = models.CharField(
        max_length=20,
        choices=ItemCurrency.choices,
        default=ItemCurrency.USD
    )

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    

class Order(models.Model):
    """Заказы продуктов"""
    item = models.ManyToManyField(Item)
