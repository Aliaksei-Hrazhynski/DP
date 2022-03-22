from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['dish']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone', 'email',
                    'address_delivery', 'date_created', 'moderation', 'paid']
    list_filter = ['date_created', 'moderation', 'paid']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
