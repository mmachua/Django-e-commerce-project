from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .decorators import userprofile_required
from .forms import  UserProfileSignUpForm
from .models import  User


class UserProfileSignUpView(CreateView):
    model = User
    form_class = UserProfileSignUpForm
    template_name = 'login/reg_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'userprofile'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:product_list')

