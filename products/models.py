from django.db import models
from uuid import uuid4
from authentication.models import UserProfile

# Create your models here.


class Product(models.Model):
        
  uuid = models.CharField(
        primary_key=True,
        unique=True,
        default=uuid4,
        max_length=100)
  name = models.CharField(max_length=255)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, related_name="user_user_profile")
  country = models.CharField(max_length=225)
  city = models.CharField(max_length=225)
  tag_code = models.CharField(max_length=225)
  condition = models.CharField(max_length=225)
  status = models.CharField(max_length=255, blank=True)
  specifications = models.TextField(blank=False)
  link = models.CharField(max_length=225)
  price = models.FloatField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
        return self.name

class Order(models.Model):
      class Types(models.TextChoices):
            ORDER = 'order'
            CHECK = 'check'
      
      class Status(models.TextChoices):
            PROCESSING = 'Processing'
            AVAILABLE = 'Available'
            OUT_OF_STOCK = 'Out of stock'
      
      uuid = models.CharField(
        primary_key=True,
        unique=True,
        default=uuid4,
        max_length=100)
      user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False)
      product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
      type = models.CharField(choices=Types.choices, max_length=255, blank=False)
      status = models.CharField(choices=Status.choices, max_length=255, blank=False)
      created_at = models.DateTimeField(auto_now_add=True)
