import json
from django.core.management.base import BaseCommand
from couponstats.models import Coupon

'''
    After running makemigrations and the migrations, use this file to import the coupons.json file.
'''
'''
    Note on parsing:
        - Null values are allowed on the 'value' field. (example: free shipping)
        - promotion types are useless if null, so we skip them.
    Promotion types and values CAN be figured out from the title, but I think that is
    out of the scope of this script. It's not reliable to determine where and which value
    is inside the title string.
    In a nutshell: we assume values can be null, but null promotion types are unacceptable.
'''
class Command(BaseCommand):

    def handle(self, *args, **options):
        json_file = './coupons.json'
        
        with open(json_file, 'r') as file:
            data = json.load(file)
            coupons = data.get('coupons', [])
            
            for coupon_data in coupons:
                if coupon_data['promotion_type'] == None:
                    continue

                Coupon.objects.create(
                    country_code=coupon_data['country_code'],
                    coupon_id=coupon_data['coupon_id'],
                    coupon_webshop_name=coupon_data['coupon_webshop_name'],
                    description=coupon_data['description'],
                    first_seen=coupon_data['first_seen'],
                    last_seen=coupon_data['last_seen'],
                    promotion_type=coupon_data['promotion_type'],
                    title=coupon_data['title'],
                    value=coupon_data['value'],
                    webshop_id=coupon_data['webshop_id']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported coupons'))