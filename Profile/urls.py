from django.urls import include, re_path
from Profile.views import ProfileView, ShopView, AboutView
from .import views
#from shop.views import product_form

app_name='Profile'

urlpatterns = [
    re_path(r'^$', ProfileView.as_view(), name='Profile'),
    re_path(r'^shop',ShopView.as_view(), name='shop'),
    re_path(r'^about', AboutView.as_view(), name='about'),
   # re_path(r'^profile/$', views.view_profile, name='view_profile'),
    re_path(r'^Profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile_with_pk'),
    #re_path(r'^(?P<category_slug>[-\w]+)/$', ProfileView.as_view(), name='user_post_by_category'),
    re_path(r'^Profile/(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProfileView.as_view(), name='user_post_detail'),
    #re_path(r'^$', views.product_list, name='product_list'),
    #re_path(r'^(?P<pk>\d+)/$', views.product_list, name='product_list_with_pk'),
    re_path(r'^product_form/$', views.product_form, name='product_form'), 
    re_path(r'^userprofile_form/$', views.userprofile_form, name= 'userprofile_form'),
]