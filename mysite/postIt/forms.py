from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'author', 'category', 'photo', 'content'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'auth_user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'category' , 'content','photo'}

    # def save(self, commit=True):
    #     post =self.instance
    #     post.title = self.cleaned_data['title']
    #     post.category = self.cleaned_data['category']
    #     post.content =self.cleaned_data['content']
    #
    #     if self.cleaned_data['photo']:
    #        post.photo = self.cleaned_data['photo']
    #
    #     if commit:
    #             post.save()
    #     return post


