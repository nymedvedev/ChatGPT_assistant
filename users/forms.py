# Импортируем модель пользователя User:
from django.contrib.auth.models import User
# Импортируем класс для создания нового пользователя:
from django.contrib.auth.forms import UserCreationForm
# Импортируем класс исключения, который используется для обработки ошибок валидации:
from django.core.exceptions import ValidationError
# Импортируем классы для аутентификации пользователя:
from django.contrib.auth.forms import AuthenticationForm, UsernameField
# Импортируем модуль, который предоставляет инструменты для создания и обработки форм:
from django import forms


class UserLoginForm(AuthenticationForm):
    """ Для авторизации пользователя. """
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    # Определяем поле ввода имени пользователя (email) с помощью класса UsernameField.
    # В качестве виджета используем forms.EmailInput (также задаются CSS-класс и текст подсказки)
    username = UsernameField(widget=forms.EmailInput(
        attrs={'class': 'form_auth_block', 'placeholder': 'Введите ваш email'}))
    # Определяем поле ввода пароля (также задаются CSS-класс и текст подсказки)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form_auth_block', 'placeholder': 'Введите пароль'}))


class UserRegistrationForm(UserCreationForm):
    """ Для регистрации нового пользователя. """
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Введите email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        """Вложенный класс, содержащий метаинформацию о форме. """
        # Указываем, что для формы используется модель User:
        model = User
        # Указываем, какие поля должны быть включены в форму (email, пароль и подтверждение пароля)
        fields = ('email', 'password1', 'password2',)

    def clean_email(self):
        """Определяет метод проверки email.
        Если email уже существует в базе данных, будет вызвано исключение ValidationError."""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже используется")
        return email

    def save(self, commit=True):
        """Переопределяет метод save для сохранения нового пользователя.
        Устанавливается имя пользователя равным его email, и вызывается метод save родительского класса."""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """Для авторизации пользователя"""
    # Определяем поле ввода имени пользователя (email)
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите email'}))
    #  Определяем поле ввода пароля:
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
