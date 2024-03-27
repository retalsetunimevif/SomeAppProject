from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to='images/', null=True, blank=True)