from django.urls import path

from . import views
from .views import HomeView, PostDetailView, MakePostView, CategoryView, \
    LikeView, MakeCommentView, FavouritesView, SearchResultsView, myPostsView, delete_my_post, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('new_post/', MakePostView.as_view(), name='make-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('favourites/', FavouritesView, name='favourites'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment', MakeCommentView.as_view(), name='new-comment'),
    path('search/', SearchResultsView, name='search_results'),
    path('myposts/', myPostsView, name='my_posts'),
    path('delete/<int:pk>', delete_my_post, name='delete-post'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update-post'),

]
