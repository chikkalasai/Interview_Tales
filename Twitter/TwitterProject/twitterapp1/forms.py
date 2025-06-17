from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
