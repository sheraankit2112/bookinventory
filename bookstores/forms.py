from django import forms
from django.contrib.auth.models import User
from django.core import validators

def username_already(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("Username already registered")

def email_already(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email already registered")






class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

    

class signup(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}),validators=[username_already])

    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email ID"}),validators=[email_already])
    store=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter your Store name"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm Password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            password=self.cleaned_data['password']
            cpassword=self.cleaned_data['cpassword']

            if password!=cpassword:
                raise forms.ValidationError("Password not match")
    
