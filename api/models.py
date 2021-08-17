from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=30)
    emp_name = models.CharField(max_length=30)
    shop_location = models.CharField(max_length=50)

    def __str__(self):
       return self.shop_name