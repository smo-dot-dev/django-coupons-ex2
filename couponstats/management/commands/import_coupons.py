import json
from django.core.management.base import BaseCommand
from couponstats.models import Coupon, PromotionType, Webshop

'''
    After running makemigrations and the migrations, use this file to import the coupons.json file.
'''
'''
    Note on parsing:
        - Null values are allowed on the 'value' field. (example: free shipping)
        - promotion types are useless if null, so we store them as 'other'.
    Promotion types and values CAN be figured out from the title, but I think that is
    out of the scope of this script. It's not reliable to determine where and which value
    is inside the title string.
'''
class Command(BaseCommand):

    def handle(self, *args, **options):
        json_file = './coupons.json'
        
        with open(json_file, 'r') as file:
            data = json.load(file)
            coupons = data.get('coupons', [])
            
            for coupon_data in coupons:
                promotion_type_name = coupon_data['promotion_type']
                
                if promotion_type_name is None:
                    promotion_type_name = 'other'

                # Get or create PromotionType instance
                promotion_type_obj, created = PromotionType.objects.get_or_create(
                    name=promotion_type_name
                )

                # Get or create Webshop instance
                webshop_obj, created = Webshop.objects.get_or_create(
                    name=coupon_data['webshop_id']
                )

                Coupon.objects.create(
                    country_code=coupon_data['country_code'],
                    coupon_id=coupon_data['coupon_id'],
                    coupon_webshop_name=coupon_data['coupon_webshop_name'],
                    description=coupon_data['description'],
                    first_seen=coupon_data['first_seen'],
                    last_seen=coupon_data['last_seen'],
                    promotion_type=promotion_type_obj,
                    title=coupon_data['title'],
                    value=coupon_data['value'],
                    webshop_id=webshop_obj
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported coupons'))