from django.contrib import admin
from home.models import Friend
from .models import Create ,Contact
from .models import Post

# Register your models here.
#admin.site.register(Comment)

#admin.site.register(Post)
admin.site.register(Create)
admin.site.register(Friend)


class PostAdmin(admin.ModelAdmin):
    list_display = ['post','user','likes', 'image','date']
    #list_filter = ['available', 'created', 'updated', 'category']
    #prepopulated_fields = {'slug': ('name',)}
   
admin.site.register(Post, PostAdmin)

 
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content','user']
admin.site.register(Contact, ContactAdmin)