from django.contrib import admin
from .models import Outflows


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('product__title',)

admin.site.register(Outflows, OutflowAdmin)
