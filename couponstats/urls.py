from django.urls import path
from . import views

urlpatterns = [
    path('stats/count/', views.count_coupons, name='count_coupons'),
    path('stats/<str:promotion_type>', views.stats, name='stats'),
    path('stats/<str:promotion_type>/retailers', views.stats_by_retailer, name='stats_by_retailer'),
    path('', views.all_stats, name='all_stats'),
]

