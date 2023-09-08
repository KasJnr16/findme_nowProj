from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    date_found = models.DateField(auto_now_add = False, null = True)
    date_lost = models.DateField(auto_now_add = False, null = True)
    location_found = models.CharField(max_length=100)
    location_lost = models.CharField(max_length=100)
    isFound = models.BooleanField(default= False)
    name_of_item_owner = models.CharField(max_length=100)
    name_of_item_finder = models.CharField(max_length=100)
    phone_number_of_item_owner = models.CharField(max_length=100)
    phone_number_of_item_finder = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'images/',null = True, blank = True)