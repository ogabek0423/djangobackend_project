from django.urls import path
from .views import LoginPageView, RegisterPageView, UserDetailView, ProfilePageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('home/', ProfilePageView.as_view(), name='home'),
    path('<int:id>/', UserDetailView.as_view(), name='u_detail')
]

