from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from shop.models import Category, Product 
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
#from cart.forms import CartAddProductForm
from django.contrib.auth.models import User 
from shop.forms import ShopCreationForm, ProductForm
from .filters import UserFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from home.models import Friend

def all_shops(request):
    #args = {'user': request.user}
    return HttpResponse('kdkdl')

@login_required
def product_list(request, category_slug=None ,pk=None):
    
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(friends,2)
    paginator = Paginator(products, 20)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    index = products.number -1
    max_index = len(paginator.page_range)
    start_index = index -5 if index >= 5 else 0 
    end_index = index + 5 if index <=max_index  -5 else max_index
    page_range = paginator.page_range[start_index:end_index]
        
    return render(request, 'shop/list.html',{'category': category,
    'categories':categories, 'products': products ,'users': users,'friends': friends,
    'product_list':product_list, 'page_range': page_range })


def listing(request):
    product_list =products.objects.all()
    paginator = Paginator(product_list, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/list.html',{'category': category,
    'categories':categories, 'products': products ,'product_list':product_list,
 })


#@method_decorator(login_required, name='dispatch')
#class ProductView(TemplateView):
#    template_name = 'shop/list.html'
#    model = Product
      # Default: <app_label>/<model_name>_list.html
#    context_object_name = 'Product'  # Default: object_list
#    paginate_by = 3
#    queryset = Product.objects.filter(available=True)
    


#    def get_queryset(self, *args, **kwargs):

#        if self.kwargs:
#            return Product.objects.filter(category=self.kwargs['category']).order_by('-created')
#        else:
#            query = Product.objects.all().order_by('-created')
#        return query

#    def get(self, request, category_slug=None ,pk=None):

#        category = None
        
        

#        products = Product.objects.filter(available=True)
#        categories = Category.objects.all()
#        users = User.objects.exclude(id=request.user.id)
#        friend = Friend.objects.get(current_user=request.user)
#        friends = friend.users.all()
        
#        if category_slug:
#            category = get_object_or_404(Category, slug=category_slug)
#            products = products.filter(category=category)

        
        #paginator = Paginator(Product, 1)
        #page = request.GET.get('page')

        #try:
        #    products = paginator.page(page)
        #except PageNotAnInteger:
        #    products = paginator.page(1)
        #except EmptyPage:
        #    products = paginator.page(paginator.num_pages)
        #index = products.number -1
        #max_index = len(paginator.page_range)
        #start_index = index -5 if index >= 5 else 0 
        #end_index = index + 5 if index <=max_index  -5 else max_index
        #page_range = paginator.page_range[start_index:end_index]

#        args = {'products': products, 'categories': categories, 'users': users,
#         'friends': friends, #'page_range': page_range, #'items': items
#         }

#        return render(request, self.template_name, args)

  


#    def listing(self, request):
#        product_list =products.objects.all()
#        paginator = Paginator(product_list, 5)
#        page = request.GET.get('page')
#        products = paginator.get_page(page)
#        return render(request,self.template_name,{'category': category,
#                               'categories':categories, 'products': products ,
#                               'product_list':product_list })



@method_decorator(login_required, name='dispatch')
class Product_detailView(TemplateView):
    template_name = 'shop/detail.html'

    def get(self, request, id , slug ,pk=None):

        if pk:
            user = User.objects.get(pk=pk)
            product = get_object_or_404(Product, user=user, slug=slug, available=True)
        else:
            user = request.user
            product = get_object_or_404(Product, id=id, slug=slug, available=True) 

        args = {'product': product, 'user': user }
        
        return render(request,self.template_name, args) 
                


class Contactview(TemplateView):
    template_name = 'shop/contact_us.html'


def contact_us(request):
    form_class = ContactForm(request.POST or None)

    return render(request, 'shop/contact_us.html', {
        'form': form_class,
    })


def AbouttView(request):
 #   #args = {'user': request.user}
    return render(request,('shop/about_uss.html'))   

def registershop(request):
    if request.method == 'POST':
        form = ShopCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop/shopp')
        else:
            form = ShopCreationForm()

           # args = ('form': form)
            return render(request, 'shop/reg_form.html')#, args)




def search(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'shop/search/product_list.html', {'filter': product_filter})

class ShopsView(TemplateView):
    template_name = 'shop/shops.html'

    def get(self, request):
        
        
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {  'users': users,
         'friends': friends
        }
        return render(request, self.template_name, args)
