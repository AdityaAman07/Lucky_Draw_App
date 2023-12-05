import pandas as pd
from django.db import models

class PartnerCoupon(models.Model):
    coupon_number = models.IntegerField(unique=True)
    ei_code = models.CharField(max_length=50)
    partner_name = models.CharField(max_length=250)
    rm_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)

    @classmethod
    def load_from_excel(cls, file_path):
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            cls.objects.create(
                coupon_number=row['coupon_number'],
                ei_code=row['ei_code'],
                partner_name=row['partner_name'],
                rm_name=row['rm_name'],
                branch=row['branch'],
                zone=row['zone'],
            )


class FLSCoupon(models.Model):
    coupon_number = models.IntegerField(unique=True)
    ei_code = models.CharField(max_length=50)
    fls_name = models.CharField(max_length=250)
    rm_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)

    @classmethod
    def load_from_excel(cls, file_path):
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            cls.objects.create(
                coupon_number=row['coupon_number'],
                ei_code=row['ei_code'],
                fls_name=row['fls_name'],
                rm_name=row['rm_name'],
                branch=row['branch'],
                zone=row['zone'],
            )


class GenerateWinnerExcel(models.Model):
    ROUND_CHOICES = [
        ('partners', 'Partners'),
        ('fls', 'FLS'),
    ]

    round_type = models.CharField(max_length=10, choices=ROUND_CHOICES)
    generated_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.round_type} Winner Excel - {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"