from django.urls import path
from .views import load_coupons, display_partnercoupons, load_flscoupons, display_flscoupons, homepage

urlpatterns = [
    path('load-coupons/', load_coupons, name='load_coupons'),   
    path('load-flscoupons/', load_flscoupons, name='load_flscoupons'),
    path('displayp/<int:amount>/', display_partnercoupons, name='display_partnercoupons'),
    path('displayf/<int:amount>/', display_flscoupons, name='display_flscoupons'),
    path('', homepage, name='homepage'),
    # Add other URLs as needed
]