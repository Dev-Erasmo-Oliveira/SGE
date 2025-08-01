from django.db import models
from products.models import Product

class Outflows(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name= 'outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Outflows"

    def __str__(self):
        return str(self.product)