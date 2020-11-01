from django.contrib import admin
from login.models import UserProfile, UserProfileClient
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('User','shop_name','user_info','city','phone', 'description')

    def user_info(self, obj):
        return obj.description

def get_queryset(self, request):
    queryset = super(UserProfileAdmin, self).get_queryset(request)
    queryset = queryset.order_by('phone','User')
    return queryset


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(UserProfileClient)