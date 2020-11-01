from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_userprofileclient = models.BooleanField(default=False)
    is_userprofile = models.BooleanField(default=False)





class UserProfileManager(models.Manager):
    pass
# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=21, default='')

    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.User.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        User_Profile = UserProfile.objects.create(User=kwargs['instance'])
        #User_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

class UserProfileClient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    city = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=6,  default='' )




