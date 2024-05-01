from django.contrib.auth import views
from users.forms import UserLoginForm
from django.urls import path
from users.views import register

urlpatterns = [
    # Путь к стр. регистрации
    path('register/', register, name='register'),
    # Домашняя страница = стр. авторизации:
    path(
        '',
        views.LoginView.as_view(
            template_name="users/signup.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    )
]
