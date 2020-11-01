from django.conf.urls import include, re_path
from .import views
from .views import  AbouttView,  all_shops
from shop.views import Product_detailView, ShopsView#, ProductView,
from home.views import Friend

app_name = 'shop'


urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
   # re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    #re_path(r'^$', ProductView.as_view(), name='product_list'),
    #re_path(r'^(?P<pk>\d+)/$',ProductView.as_view() , name='product_list_with_pk'),
    re_path(r'^$', ShopsView.as_view(), name='shops'),
    #re_path(r'^$', views.ShoppView, name='shopp'),
    #re_path(r'^(?P<category_slug>[-\w]+)/$', ProductView.as_view(), name='product_list_by_category'),
    #re_path(r'^(?P<pk>[-\w]+)/$',ProductView.as_view(), name= 'product_list_by_category_with_pk' ),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', Product_detailView.as_view(), name='product_detail'),
    re_path(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', Product_detailView.as_view(), name='product_detail_with_pk'),
    re_path(r'^about_uss/$',views.AbouttView, name='about_uss'),
    re_path(r'^contact_us/$', views.contact_us , name='contact_us'),
    re_path(r'^registershop/$', views.registershop, name='registershop'), 
    #re_path(r'^product_form/$', views.product_form, name='product_form'), 
    re_path(r'^search/$', views.search, name='search'),  
    re_path(r'^all_shops/$', views.all_shops, name='all_shops'),
    #re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', 
    #        views.change_friends, name='change_friends'),
]

