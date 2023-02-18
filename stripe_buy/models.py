from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self) -> str:
        return self.name

class Discount(models.Model):

    DURATION_CHOICES = (
        ('once', 'ONCE'),
        ('forever', 'FOREVER'),
        ('repeating', 'REAPITING'),
    )

    duration = models.CharField(choices=DURATION_CHOICES, max_length=10, default='ONCE')
    dis_id = models.CharField(max_length=255)
    percent_off = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'Discount for {self.percent_off} %'

class Tax(models.Model):

    display_name = models.CharField(max_length=10)
    percentage = models.PositiveIntegerField()
    inclusive = models.BooleanField()

    def __str__(self) -> str:
        return f'The {self.display_name} Tax'

class Order(models.Model):

    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    taxes = models.ManyToManyField(Tax)
    items = models.ManyToManyField(Item, through='OrderToItem')

    def __str__(self) -> str:
        return f'Order #{self.id}'

class OrderToItem(models.Model):

    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

