from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #,UserProfile
from django.contrib.auth.models import User
from .models  import UserProfile



class UserProfileSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        User = super(UserProfileSignUpForm, self).save(commit=False)
        User.first_name = self.cleaned_data['first_name']
        User.last_name = self.cleaned_data['last_name']
        User.email = self.cleaned_data['email']

        user = super().save(commit=False)
        user.is_userprofile = True
        if commit:
            user.save()
        return user


class UserProfileClientSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #super().__init__(strip=True, **kwargs)

    class Meta:
        model = User
        fields = ( 
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        User = super(UserProfileClientSignUpForm, self).save(commit=False)
        User.first_name = self.cleaned_data['first_name']
        User.last_name = self.cleaned_data['last_name']
        User.email = self.cleaned_data['email']

        User.is_userprofileclient = True
       

        if commit:
            User.save()

        return User


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'shop_name',
            'description',
            'city',
            'website',
            'phone',
            'image'
        )

    def save(self, commit=True):
        User = super(UserProfileForm, self).save(commit=False)
        User.shop_name = self.cleaned_data['shop_name']
        User.description = self.cleaned_data['description']
        User.city = self.cleaned_data['city']
        User.website = self.cleaned_data['website']
        User.phone = self.cleaned_data['phone']
        User.image = self.cleaned_data['image']

        if commit:
            User.save()

        return User


            




class contactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True)