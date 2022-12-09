from django.db import models

class DynamicCleaningFeeCalculation(models.Model):
    cleaner_payout = models.DecimalField(max_digits=6, decimal_places=2)
    clean_flat_rate = models.DecimalField(max_digits=6, decimal_places=2)
    clean_dynamic_rate_1 = models.DecimalField(max_digits=6, decimal_places=2)
    clean_dynamic_rate_2 = models.DecimalField(max_digits=6, decimal_places=2)
    clean_dynamic_rate_3 = models.DecimalField(max_digits=6, decimal_places=2)
    clean_dynamic_rate_4 = models.DecimalField(max_digits=6, decimal_places=2)

