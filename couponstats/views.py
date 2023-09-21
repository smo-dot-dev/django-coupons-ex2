from django.http import JsonResponse
from django.db.models import Count, Min, Max, Avg
from .models import Coupon, PromotionType, Webshop
from django.db.models import F

# How many coupons each coupon type has?
# /coupons/count
def count(request):
    data = list(PromotionType.objects
                .annotate(count=Count('coupon'))
                .values('name', 'count'))
    return JsonResponse(data, safe=False)

# Number of coupons with discount, the minimum discount, maximum discount, and average discount for percent-off/dollar-off coupons
# /coupons/stats/<str:promotion_type>
def stats(request, promotion_type):
    data = (Coupon.objects
                .filter(promotion_type__name=promotion_type)
                .aggregate(** {
                    'num_coupons': Count('id'),
                    'min_discount': Min('value'),
                    'max_discount': Max('value'),
                    'avg_discount': Avg('value')
            }))

    data['avg_discount'] = round(data['avg_discount'], 2) if data['avg_discount'] else 0
    return JsonResponse(data, safe=False)

# Same as above, but grouped by retailer
# /coupons/stats/<str:promotion_type>/retailers
def stats_by_retailer(request, promotion_type):
    data = list(Coupon.objects
                .filter(promotion_type__name=promotion_type)
                .annotate(webshop=F('webshop_id__name'))  
                .values('webshop')
                .annotate(**{
                    'num_coupons': Count('id'),
                    'min_discount': Min('value'),
                    'max_discount': Max('value'),
                    'avg_discount': Avg('value')
                }))

    for item in data:
        item['avg_discount'] = round(item['avg_discount'], 2) if item['avg_discount'] else 0
    return JsonResponse(data, safe=False)
