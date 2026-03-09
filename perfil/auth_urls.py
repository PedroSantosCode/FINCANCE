from django.urls import path
from . import auth_views

urlpatterns = [
    path('login/', auth_views.login_view, name='auth_login'),
    path('logout/', auth_views.logout_view, name='auth_logout'),
]
