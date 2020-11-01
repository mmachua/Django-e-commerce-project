
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
#from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.forms import HomeForm, HomeCreate
from home.models import Post, Friend
from .models import Create
from home.forms import ContactForm
from login.models import UserProfile
from .models import Friend
from django.utils.decorators import method_decorator


@login_required
def home(request):
    return render(request, 'core/home.html')



@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/home.html'    
    #@login_required
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
      
        args = {'form': form, 'posts': posts, 'users': users,
         'friends': friends
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid(): 
            image = form.save(commit=False)
            post = form.save(commit=False)
            post = get_object_or_404(Post, id=id, slug=slug)
            is_liked = False
            #if post.likes.filter(user=request.user) and True or False
            #   is_liked = True
            post.user = request.user
            post.save()
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            form = HomeForm()
            return redirect('home:home')
        args = {'form': form, 'post': post, 'image': image,
         'is_liked': is_liked  }
        return render(request, self.template_name, args)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.post.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())    

@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home') 




class CreateView(TemplateView):
    template_name = 'home/create.html'
    #Create = Create.objects.all()[:10]

    def get(self, request):
        form = HomeCreate()
        posts = Post.objects.all()
       # friend = Friend.objects.get(current_user=request.user)
        #friends = friend.users.all()

        args = {'form':form, 'posts':posts ,  }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeCreate(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            bizname = form.cleaned_data[ 'bizname' ]
            te = form.cleaned_data[ 'location']
            phone = form.cleaned_data['phone']
            form = HomeCreate()
            #form.save()
            

        args = {'form':form , 'bizname': bizname, 'te':te, 'phone':phone }
        return render(request, self.template_name, args)




class ShopView(TemplateView):
    template_name = 'home/shop.html' 

    def Shop(self, request, pk=None):
        if pk:
            shop = shop.objects.get(pk=pk)
        else:
            shop = request.shop
        return render(request,('home/shop.html'), {'shop': shop})


class AboutView(TemplateView):
    template_name = 'home/About.html'  



#@login_required
def shop(request):
    #args = {'user': request.user}
    return render(request,('home/shop.html'), {'user': request.user})


#contact form views are here
def contact(request):
    form_class = ContactForm(request.POST or None)

    return render(request, 'home/contact.html', {
        'form': form_class,
    })

def search_posts(self, request):
        if request.method == "POST":
            search_text = request.POST['search_text']
        else:
            search_text = ''
    
        posts = Post.objects.filter(title__contains=search_text)

        return render_to_response('ajax_search.html', {'posts': posts})
        