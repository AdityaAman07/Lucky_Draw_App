import random
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import PartnerCoupon, FLSCoupon, GenerateWinnerExcel


# Reward_List = ['Amazon Gift Voucher', 'Steel Coffee Mug', 'Laptop Bag', 'Bluetooth Airdopes', 'RenewBuy Branded kit', 'Smart Watch', 'Sliver Coin', 'Gold Coin', 'IPhone 15']

def load_coupons(request):
    PartnerCoupon.load_from_excel('coupon/data/partners_excel.xlsx')
    return HttpResponse("Partner Coupons loaded successfully.")


def load_flscoupons(request):
    FLSCoupon.load_from_excel('coupon/data/fls_excel.xlsx')
    return HttpResponse("FLS Coupons loaded successfully.")

def display_partnercoupons(request, amount):
    available_partner_coupons = PartnerCoupon.objects.filter(displayed=False)
    selected_partner_coupons = random.sample(list(available_partner_coupons), min(amount, len(available_partner_coupons)))
    
    for coupon in selected_partner_coupons:
        coupon.displayed = True
        coupon.save()
    

    GenerateWinnerExcel.objects.create(round_type='partners' if selected_partner_coupons else 'fls')

    

    # selected_coupons = PartnerCoupon.objects.order_by('?')[:amount]
    context = {
        'partner_coupons': selected_partner_coupons,
        # 'coupons': selected_coupons,
        # 'reward_value': reward_value,
    }
    return render(request, 'index.html', context)


def display_flscoupons(request, amount):
    available_fls_coupons = FLSCoupon.objects.filter(displayed=False)
    selected_fls_coupons = random.sample(list(available_fls_coupons), min(amount, len(available_fls_coupons)))
    
    for coupon in selected_fls_coupons:
        coupon.displayed = True
        coupon.save()
    

    GenerateWinnerExcel.objects.create(round_type='fls' if selected_fls_coupons else 'partners')


    # fls_coupons = FLSCoupon.objects.order_by('?')[:amount]
    context = {
        'coupons': selected_fls_coupons,
    }
    return render(request, 'fls.html', context)


def generate_winner_excel(coupons, file_path):
    # print(coupons)
    df = pd.DataFrame(coupons)
    df.to_excel(file_path, index=False)

def display_partnercoupons(request, amount):
    selected_partner_coupons = PartnerCoupon.objects.order_by('?')[:amount]

    # Generate winner Excel file for the current display amount
    generate_winner_excel(selected_partner_coupons.values(), f'coupon/data/Partners_winners_{amount}.xlsx')


    # reward_value = str(Reward_List[int(button_value)])
    # for coupon in selected_partner_coupons:
    #     coupon.reward = reward_value
    #     coupon.save()


    context = {
        'coupons': selected_partner_coupons,
        # 'reward': reward_value,
        
    }
    return render(request, 'index.html', context)


def display_flscoupons(request, amount):
    fls_coupons = FLSCoupon.objects.order_by('?')[:amount]

    # Generate winner Excel file for the current display amount
    generate_winner_excel(fls_coupons.values(), f'coupon/data/FLS_winners_{amount}.xlsx')

    context = {
        'coupons': fls_coupons.values(),
    }
    return render(request, 'fls.html', context)


def homepage(request):
    return render(request, 'demo.html')






# from django.shortcuts import render, HttpResponse
# from .models import PartnerCoupon, FLSCoupon, generate_winner_excel
# import random

# def load_coupons(request):
#     PartnerCoupon.load_from_excel('coupon/data/partners_excel.xlsx')
#     FLSCoupon.load_from_excel('coupon/data/fls_excel.xlsx')
#     return HttpResponse("Coupons loaded successfully.")

# def display_coupons(request, amount):
#     # Assuming PartnerCoupon and FLSCoupon models have a 'displayed' field
#     # Ensure to modify your models to include such a field if not present

#     # Get available coupons that have not been displayed
#     available_partner_coupons = PartnerCoupon.objects.filter(displayed=False)
#     available_fls_coupons = FLSCoupon.objects.filter(displayed=False)

#     # Randomly select coupons based on the given amount
#     selected_partner_coupons = random.sample(list(available_partner_coupons), min(amount, len(available_partner_coupons)))
#     selected_fls_coupons = random.sample(list(available_fls_coupons), min(amount, len(available_fls_coupons)))

#     # Mark selected coupons as displayed
#     for coupon in selected_partner_coupons:
#         coupon.displayed = True
#         coupon.save()

#     for coupon in selected_fls_coupons:
#         coupon.displayed = True
#         coupon.save()

#     # Add a 'Reward' column with the button value
#     reward_value = f"Display {amount}"
#     for coupon in selected_partner_coupons:
#         coupon.reward = reward_value
#         coupon.save()

#     for coupon in selected_fls_coupons:
#         coupon.reward = reward_value
#         coupon.save()

#     context = {
#         'partner_coupons': selected_partner_coupons,
#         'fls_coupons': selected_fls_coupons,
#         'reward_value': reward_value,
#     }

#     return render(request, 'index.html', context)