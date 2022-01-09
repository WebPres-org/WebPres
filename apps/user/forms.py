from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.user.models import Profile
from apps.user import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

##Add New
class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'facebook_url', 'twitter_url','website_url', 'instagram_url' ]


class ProfilePageForm(forms.ModelForm):
    model = Profile
    fields = ['bio', 'avatar', 'facebook_url', 'twitter_url','website_url', 'instagram_url' ]
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
