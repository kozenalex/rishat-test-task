from django.contrib import admin
from stripe_buy.models import Item, Order, OrderToItem, Discount, Tax
# Register your models here.

class OrderInline(admin.TabularInline):

    model = OrderToItem
    extra = 3

class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderInline,)

admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
admin.site.register(Tax)