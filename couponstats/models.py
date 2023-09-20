from django.db import models


# Create your models here.
class Coupon(models.Model):
    country_code = models.CharField(max_length=2, default='us')
    coupon_id = models.PositiveIntegerField(unique=True)
    coupon_webshop_name = models.CharField(max_length=255)
    description = models.TextField()
    first_seen = models.DateField()
    last_seen = models.DateField()
    
    # Choices for promotion_type field
    PROMOTION_TYPES = [
        ('percent-off', 'Percent Off'),
        ('buy-one-get-one', 'Buy One Get One'),
        ('dollar-off', 'Dollar Off'),
        ('free-gift', 'Free Gift'),
        ('free-shipping', 'Free Shipping'),
    ]
    promotion_type = models.CharField(
        max_length=20,
        choices=PROMOTION_TYPES,
        default='percent-off',
    )

    title = models.CharField(max_length=255)
    value = models.PositiveIntegerField()
    webshop_id = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} ({self.coupon_id})'