from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflows


@receiver(post_save, sender=Outflows)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()