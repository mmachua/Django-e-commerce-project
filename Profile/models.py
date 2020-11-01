from __future__ import unicode_literals
#from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from login.models import UserProfile
#from django.contrib.auth import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse




class About(models.Model):
    logo = models.ImageField( upload_to='posts/%Y/%m/%d',null=True, blank=True)
    location = models.CharField(max_length=500)
    dealers_in = models.CharField(max_length=500)
    image = models.ImageField( upload_to='posts/%Y/%m/%d',null=True, blank=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    date = models.DateTimeField(auto_now=True)
    
    
    
    
    