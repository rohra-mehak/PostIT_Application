from django.urls import path
from .views import UserRegisterView, UserEditView, ProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='show_profile'),
]