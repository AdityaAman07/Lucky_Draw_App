from django.contrib import admin
from .models import PartnerCoupon, FLSCoupon, GenerateWinnerExcel




@admin.register(PartnerCoupon)
class PartnerCouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_number', 'ei_code', 'partner_name', 'rm_name', 'branch', 'zone')
    search_fields = ('coupon_number', 'ei_code', 'partner_name', 'rm_name', 'branch', 'zone')

@admin.register(FLSCoupon)
class FLSCouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_number', 'ei_code', 'fls_name', 'rm_name', 'branch', 'zone')  # Add other fields for FLS
    search_fields = ('coupon_number', 'ei_code', 'fls_name', 'rm_name', 'branch', 'zone')  # Add other fields for FLS


admin.site.register(GenerateWinnerExcel)