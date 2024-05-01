from django.db import models
from django.contrib.auth.models import User

# класс для профилей пользователей,
# содержит 2 параметра: логин, почта.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)

