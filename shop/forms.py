from django import forms
from django.contrib.auth.models import User
from .models import Product



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class ShopCreationForm(forms.Form):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = (
            'shop_name',
            'shop_contact',
            'last_name',
            ' shop_email',
            
        )
    def save(self, commit=True):
        User = super(ShopCreationForm, self).save(commit=False)
        User.shop_name = self.cleaned_data['first_name']
        User.shop_name = self.cleaned_data['last_name']
        User.shop_email = self.cleaned_data['email']

        if commit:
            User.save()

        return User



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'slug', 
            'image',
            'image2',
            'image3',
            'description',
            'price',
            'stock',
            'available',
           
            )
    def save(self,commit=True):
        User = super(ProductForm, self).save(commit=False)
        User.category = self.cleaned_data['category']
        User.name = self.cleaned_data['name']
        User.slug = self.cleaned_data['slug']
        User.image = self.cleaned_data['image']
        User.image2 = self.cleaned_data['image2']
        User.image3 = self.cleaned_data['description']
        User.price = self.cleaned_data['price']
        User.stock = self.cleaned_data['category']
        User.Available = self.cleaned_data['available']
        User.user = self.cleaned_data['user']

        if commit:
            Product.save()

        return Product
    

