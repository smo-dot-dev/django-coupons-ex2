from rest_framework import serializers
from .models import Coupon, CouponType, Webshop

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class CouponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponType
        fields = '__all__'

class WebshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webshop
        fields = '__all__'