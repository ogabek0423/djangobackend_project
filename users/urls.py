from django.urls import path
from .views import UserListView, UserSettingView, UserLoginView, UserRegisterView, UserLoginForm, UserRegisterForm, UserDetailView, HomePageView, ProfileView
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('home/', HomePageView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:id>/', UserDetailView.as_view(), name='users-detail'),
    path('setting/<int:id>/', UserSettingView.as_view(), name='settings'),
    path('profile/', ProfileView.as_view(), name='profile')
]

