from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="profiles", on_delete=models.SET_NULL)
    avatar = models.ImageField(upload_to="pictures", default="avatar.png")
    identity_num = models.CharField(max_length=11, blank=True, null=True)
    iban = models.CharField(max_length=26, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    plate_num = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    insurance_num = models.CharField(max_length=50, blank=True, null=True)
    insurance_company = models.CharField(max_length=25, blank=True, null=True)
