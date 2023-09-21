from django.db import models


# Create your models here.
class Coupon(models.Model):
    country_code = models.CharField(max_length=2, default='us')
    '''
        I did not put unique=True on coupon_id because id 260310 is duplicated in the JSON file.
        Besides, we can assume Django will automatically create a unique id for each coupon.
        Ideally, we should know where the ID comes from, to tell if it is unique or not.
    '''
    coupon_id = models.PositiveIntegerField()
    coupon_webshop_name = models.CharField(max_length=255)
    description = models.TextField()
    first_seen = models.DateField()
    last_seen = models.DateField()
    promotion_type = models.ForeignKey(
        'PromotionType',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=255)
    value = models.PositiveIntegerField(null=True)
    webshop_id = models.ForeignKey(
        'Webshop',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.title} ({self.coupon_id})'

class PromotionType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class Webshop(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name