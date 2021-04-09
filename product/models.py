from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weight(models.Model):
    weight_range=models.CharField(max_length=255, unique=True)
    price=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.weight_range} / {self.price}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Product(models.Model):
    STATUS_CHOICE=(
        ('pending','PENDING'),
        ('delivered', 'DELIVERY'),
        ('return', 'RETURN')
    )
    weight=models.ForeignKey(Weight, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    fullname=models.CharField(max_length=255)
    contact1=models.CharField(max_length=255)
    contact2=models.CharField(max_length=255, null=True, blank=True)
    address=models.CharField(max_length=255)
    shipping_address=models.CharField(max_length=255)
    status=models.CharField(max_length=50 , choices=STATUS_CHOICE)
    remarks=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='product_image/', blank=True, null=True)

    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.status='pending'
        super().save(*args, **kwargs)
