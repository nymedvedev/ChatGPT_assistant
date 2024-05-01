"""Этот фрагмент кода представляет собой определение класса конфигурации приложения FormsConfig
 в файле forms/apps.py проекта Django.
from django.apps import AppConfig - Импортирует класс AppConfig из модуля django.apps.
 Этот класс является базовым классом для конфигурации приложений Django.
class FormsConfig(AppConfig): - Определяет класс FormsConfig, наследующийся от класса AppConfig.
 Этот класс используется для конфигурации приложения forms.
default_auto_field = 'django.db.models.BigAutoField'
 - Устанавливает значение по умолчанию для автоматического поля (auto-field) в моделях приложения forms.
  В этом случае используется BigAutoField, который является полем с автоинкрементным целым числом большого размера.
   Это означает, что при создании новых моделей в приложении forms будет использоваться BigAutoField
   для первичных ключей, если не будет указан другой тип поля.
name = 'forms' - Устанавливает имя приложения, для которого используется данная конфигурация.
В этом случае имя приложения - 'forms'. Этот атрибут обязателен для классов конфигурации приложений Django.
"""

from django.apps import AppConfig

class FormsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forms'
