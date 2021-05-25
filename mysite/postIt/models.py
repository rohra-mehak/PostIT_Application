from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    class Categories(models.TextChoices):
        WORLD = 'world'
        ENVIRONMENT = 'environment'
        TECHNOLOGY = 'technology'
        DESIGN = 'design'
        CULTURE = 'culture'
        BUSINESS = 'business'
        POLITICS = 'politics'
        OPINION = 'opinion'
        SCIENCE = 'science'
        HEALTH = 'health'
        STYLE = 'style'
        TRAVEL = 'travel'

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.OPINION)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to="images/")
    video_file = models.FileField(null = True, blank = True ,upload_to="videos/")
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='site_post')
    no_of_likes = models.IntegerField(default=0)
    no_of_dislikes = models.IntegerField(default=0)
    favourite = models.BooleanField(default=False)


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.post.id)))