# filmrating/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from ratings import views as ratings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ratings_views.home, name='home'),
    path('ratings/', include('ratings.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='ratings/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/register/', ratings_views.register, name='register'),
    path('accounts/profile/', ratings_views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
