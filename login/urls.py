from django.conf.urls import url
from django.urls import include, re_path
from django.urls import include ,path
from django.contrib.auth.views import (
    login,
    logout,
     password_reset_confirm,
      password_reset,
     password_reset_done,
     password_reset_complete
     )
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from . import views
from login.views import ProfileView #, userprofile_form

app_name = 'login'
urlpatterns = [
    #re_path(r'^$', views.index),
    re_path(r'^accounts/$', login,{'template_name': 'login/accounts.html'}, name='login'),
    re_path(r'^logout/$', logout,{'template_name': 'login/logout.html'}, name='logout'),
    re_path(r'^register/$', views.register, name='register'),

    #re_path(r'^profile/$', views.view_profile, name='view_profile'),
    re_path(r'^profile/$', ProfileView.as_view(), name='view_profile'),
    #re_path(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile_with_pk'),
    #re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    #re_path(r'^userprofile_form/$', views.userprofile_form, name= 'userprofile_form'),
    re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    re_path(r'^change-password/$', views.change_password, name='change_password'),
    re_path(r'^about/$', views.about, name='about'),

    re_path(r'^reset-password/$', password_reset,{ 'template_name':
    'login/reset_password.html','post_reset_redirect':
    'login:password_reset_done','email_template_name':
    'login:reset_password_email.html' }, name='reset_password'),

    re_path(r'^reset-password/done/$', password_reset_done, 
    {'template_name':'login/reset_password_done.html'},
     name='password_reset_done'),

    #url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),
    
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     password_reset_confirm, {'template_name':
     'login/reset_password_confirm.html', 'post_reset_redirect':
     'login:password_reset_complete'},  name='password_reset_confirm'),

    re_path(r'^reset-password/complete/$', password_reset_complete,{'template_name':
    'login/reset_password_complete.html'}, name='password_reset_complete')

]