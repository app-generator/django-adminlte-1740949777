# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    id = models.ForeignKey(Cart, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Customer(models.Model):

    #__Customer_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Cart(models.Model):

    #__Cart_FIELDS__
    cart_registration_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    #__Cart_FIELDS__END

    class Meta:
        verbose_name        = _("Cart")
        verbose_name_plural = _("Cart")



#__MODELS__END
