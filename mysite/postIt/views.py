from django.shortcuts import render, redirect
from django.http import HttpResponse
# from . import forms as f
from .forms import RegistrationForm
# from forms import RegistrationForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class MakePostView(CreateView):
    model = Post
    template_name = 'make_post.html'
    fields = ('title', 'author', 'category', 'content', 'photo')
