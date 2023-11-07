from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ...
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Add your custom views and URL patterns as needed.
]