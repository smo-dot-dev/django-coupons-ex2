from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.count, name='count'),
    path('stats/<str:promotion_type>', views.stats, name='stats'),
    path('stats/<str:promotion_type>/retailers', views.stats_by_retailer, name='stats_by_retailer'),
]

