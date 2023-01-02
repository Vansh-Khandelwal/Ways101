from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    profileImg = models.IntegerField(default=1)
    pass




