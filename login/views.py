
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import RegistrationForm
from .forms import (UserProfileClientSignUpForm, UserProfileSignUpForm, EditProfileForm, UserProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import contactForm
from home.views import Post
from home.models import Post, Friend
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
#from login.models import UserProfile
from shop.models import Product, Category
from .decorators import userprofileclient_required, userprofile_required




def about(request):
    context = locals()
    
    form = contactForm(request.POST or None)

    if form.is_valid():
        print( request.POST)
        context = locals()
    return render(request, 'login/about.html',context )
 
def register(request):
    if request.method =='POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             raw_password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=raw_password)
             login(request, user)
             return redirect( 'home:home' )
    else: 
        form = RegistrationForm()
        #form = {'form': form}

        #args = {'form': form}
    return render(request, 'login/reg_form.html',{'form': form} )



@method_decorator([login_required,userprofileclient_required], name='dispatch')
class ProfileView(TemplateView):
    template_name = 'login/profile.html'
    
    def get(self, request):
       

        user = request.user
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {
                 'user': user,
                 'users': users,
         'friends': friends
        }
        return render(request, self.template_name, args)

    def post_detail(self, request, id, slug):
        user_posts = get_object_or_404(Post, id=id, slug=slug, available=True)
        return render(request, 'Profile/detail.html', {'user_posts': user_posts })

#@login_required
#def userprofile_form(request):
#    if request.method == 'POST':
#        form = UserProfileForm(request.POST, instance=request.user)
#
#        if form.is_valid():
#            form.save()
#            return redirect('login:userprofile_form')
#        
#        else:
#            form = UserProfileForm(instance=request.user)
#            args = {'form': form}
#            return render(request, 'login:userprofile_form.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'login:view_profile' )

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user )

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect( 'login:view_profile' )

        else:
            return redirect('/login/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
@login_required
def login_admin(request):
    return render(request, 'admin/login.html') 