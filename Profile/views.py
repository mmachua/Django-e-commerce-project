from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from home.models import Post
from django.views.generic import (ListView)
from django.utils.decorators import method_decorator
from shop.models import Product, Category, Shop
from django.core.paginator import Paginator
from Profile.models import About
from types import MethodType
from operator import attrgetter
from shop.forms import ProductForm
from login.forms import UserProfileForm
from login.models import UserProfile



@login_required
def product_form(request):
    if request.method =='POST':
         form = ProductForm(request.POST)
         if form.is_valid():
             form.save()
             
             return redirect( 'Profile:product_form' )
    else: 
        form = ProductForm()
        #form = {'form': form}

        #args = {'form': form}
    return render(request, 'Profile/product_form.html',{'form': form} )



@login_required
def userprofile_form(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Profile:userprofile_form')
        
    else:
        
        form = UserProfileForm()
        #args = {'form': form}
        return render(request, 'Profile/userprofile_form.html', {'form': form})

class ShopView(TemplateView):
    template_name = 'Profile/shop.html'
    model = User
    paginate_by = 1
    context_object_name = 'users'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)

        args = {'users':users}
        return render(request, self.template_name, args)



@method_decorator(login_required, name='dispatch')
class AboutView(TemplateView):
    template_name = 'Profile/about.html'

    def get(self, request, pk=None):

        if pk:
            user = User.objects.get(pk=pk)
            user_about = About.objects.filter(user=user)
        else:
            user = request.user
            user_about = About.objects.filter(user=request.user.id)
        
        args = {'user_about': user_about ,'user': user}
        return render (request, self.template_name, args)

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'Profile/Profile.html'
    
    def get(self, request, category_slug=None, pk=None):
        category = None
        context = {}

        #user_products = Product.objects.filter(available=True)
        #categories = Category.objects.all()
       # if category_slug:
       #     category = get_object_or_404(Category, slug=category_slug)
        #    products = products.filter(category=category)

        if pk:
            category = None
            user = User.objects.get(pk=pk)
            user_posts = Post.objects.filter(user=user).order_by('-date')
            products = Product.objects.filter(user=user).order_by('-updated')
            category = Category.objects.filter(user=user)
            shop = Shop.objects.filter(user=user)


            #current_page = Paginator(products, 10)

            #page = request.GET.get('page')
            #try:
            #    context['product_lists'] = current_page.page(page)
            #except PageNotAnInterger:
            #    context['product_lists'] = current_page.page(1)
            #except EmptyPage:
            #    context['product_lists'] = current_page.page(current_page.num_pages)
        else:
            category = None
            user = request.user
            user_posts = Post.objects.filter(user=request.user.id).order_by('-date')
            products = Product.objects.filter(user=request.user.id).order_by('-updated')
            category = Category.objects.filter(user=request.user.id)
            shop = Shop.objects.filter(user=request.user.id)

        args = { 'user_posts': user_posts,'shop' : shop,
                 'user' : user, 'products' : products, 'category' : category,
                 #'categories': categories
         
        }
        return render(request, self.template_name, args)

    def post_detail(self, request, id, slug):
        user_posts = get_object_or_404(Post, id=id, slug=slug, available=True)
        return render(request, 'Profile/detail.html', {'user_posts': user_posts })
