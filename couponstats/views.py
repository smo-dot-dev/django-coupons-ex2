from django.http import JsonResponse
from django.db.models import Count, Min, Max, Avg
from .models import Coupon, PromotionType, Webshop
from django.db.models import F
from django.shortcuts import render


# How many coupons each coupon type has?
# stats/count
def count_coupons(request):
    data = list(PromotionType.objects
                .annotate(count=Count('coupon'))
                .values('name', 'count'))
    return JsonResponse(data, safe=False) if request else data

# Number of coupons with discount, the minimum discount, maximum discount, and average discount for percent-off/dollar-off coupons
# /stats/<str:promotion_type>
def stats(request, promotion_type):
    data = (Coupon.objects
                .filter(promotion_type__name=promotion_type)
                .aggregate(** {
                    'num_coupons': Count('id'),
                    'min_discount': Min('value'),
                    'max_discount': Max('value'),
                    'avg_discount': Avg('value')
            }))
    
    return JsonResponse(data, safe=False) if request else data

# Same as above, but grouped by retailer
# /stats/<str:promotion_type>/retailers
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
    
    return JsonResponse(data, safe=False) if request else data

'''
    Ideally, the 'request' parameter above should never be 'None', but in this case,
    these endpoints are read-only and we don't use the request object, 
    so I'm "recycling" the code above to display the data neatly.
'''
def all_stats(request):
    # Get data for 'Count by Coupon Type'
    count_data = count_coupons(None)
    # Get data for 'Stats by Coupon Type'
    percent_off_data = stats(None, 'percent-off')
    dollar_off_data = stats(None, 'dollar-off')
    # Get data for 'Stats by Retailer'
    percent_off_retailer_data = stats_by_retailer(None, 'percent-off')
    dollar_off_retailer_data = stats_by_retailer(None, 'dollar-off')

    # Prepare the context for the template
    context = {
        'count_data': count_data,
        'percent_off_data': percent_off_data,
        'dollar_off_data': dollar_off_data,
        'percent_off_retailer_data': percent_off_retailer_data,
        'dollar_off_retailer_data': dollar_off_retailer_data,
    }

    return render(request, 'all_stats.html', context)