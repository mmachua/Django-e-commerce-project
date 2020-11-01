from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_userprofile:
            return redirect('shop:product_list')
        else:
            return redirect('shop:product_list')
    return render(request, 'shop/product_list.html')  