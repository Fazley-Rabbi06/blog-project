from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    profile_pic=models.ImageField(upload_to='profile_pics')

  