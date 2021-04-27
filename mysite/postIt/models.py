from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    content = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)
    no_of_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def __str__(self):
        return str(self.user)
