from django.urls import path

from . import views
from .views import HomeView, PostDetailView, MakePostView, CategoryView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('new_post/', MakePostView.as_view(), name='make-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
