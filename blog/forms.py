from django import forms
#from .models import Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')


class PostForm(forms.ModelForm):
class Meta:
    model = Post
    fields = ('__all__',)