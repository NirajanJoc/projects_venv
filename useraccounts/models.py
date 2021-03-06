from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=255)
    avtar=models.ImageField(upload_to='avatar/', null=True, blank=True)
    bank_name=models.CharField(max_length=255, null=True, blank=True)
    bank_branch= models.CharField(max_length=255, null=True, blank=True)
    account_number=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
