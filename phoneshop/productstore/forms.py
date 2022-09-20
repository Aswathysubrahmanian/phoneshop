from django import forms
from django.forms import ModelForm
from productstore.models import mobiles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class phoneForm(ModelForm):
    class Meta:
        model=mobiles
        fields="__all__"
        widgets={
            "phone_name":forms.TextInput(attrs={"class":"form-control"}),
            "processor": forms.TextInput(attrs={"class": "form-control"}),
            "ram": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"})
        }


class UserRegForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),

        }

class SignIn(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

# class phoneForm(forms.Form):
#     phone_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     processor=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     ram=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"]
#         if price<0:
#             msg="invalid price range"
#             self.add_error("price",msg)
#
# class change_details(forms.Form):
#     phone_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     processor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     ram = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data["price"]
#         if price < 0:
#             msg = "invalid price range"
#             self.add_error("price", msg)
#
class PhoneSearch(forms.Form):
    phone_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))