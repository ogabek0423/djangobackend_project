from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('library.urls')),
    path('', LandingPageView.as_view(), name='landing-page'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

