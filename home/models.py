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


class Category(models.Model):
    #name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=2000, db_index=True, unique=True)

    class Meta:
        #ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name



class Post(models.Model):
    post = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, db_index=True ,default=True)
    image = models.ImageField( upload_to='posts/%Y/%m/%d',null=True, blank=True)
    likes = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="likes", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #authors = models.ManyToManyField(User)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post

    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_repath(self):
        return reverse('Profile:post_detail',kwargs={"slug":self.slug})

    

class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name="owner", null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend,created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend,created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
    
    def __str__(self):
        return str(self.current_user)

    def user(self):
        return self.users.count()
    

# Create your models here.
class Create(models.Model):
    Bizname = models.CharField(max_length=200)
    Location = models.TextField()
    Phone = models.CharField(max_length=14)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    #created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Bizname 


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name