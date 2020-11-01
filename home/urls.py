from django.conf.urls import url
from django.urls import include, re_path
from home.views import HomeView, CreateView,ShopView,AboutView #, ContactView
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from home import views
from . import views 

app_name = 'home'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', 
            views.change_friends, name='change_friends'),
    re_path(r'^like/$', views.like_post, name='like_post'),

    re_path(r'^create/$', CreateView.as_view(), name='create'),
    re_path(r'^shop/$', ShopView.as_view(), name='shop'),
    re_path(r'^shop/(?P<pk>\d+)/$',  ShopView.as_view(), name='shop_with_pk'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'contact/$', views.contact, name='contact'),
    #re_path(r'^search/$', views.post, name='search_posts')
    #re_path(r'^contact/$', ContactView.as_view(), name='contact')
    #re_path(r'^create/$', HomeView.as_view(), name='create')
    #re_path(r'^home/$',)
]


