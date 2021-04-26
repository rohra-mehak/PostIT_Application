from django.urls import path

from . import views
from .views import HomeView, PostDetailView, MakePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('new_post/', MakePostView.as_view(), name='make-post'),
]
