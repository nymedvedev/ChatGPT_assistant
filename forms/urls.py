from django.urls import path
# импортирую вьюхи:
from forms.views import request_form, forms_output, view_answer, update_answer

urlpatterns = [
    # Путь к странице с первоначальным запросом:
    path('ChatGPT_helper/', request_form, name='ChatGPT_helper'),
    # Путь для перехода к форме с ответом, делает редирект на 'view_answer/'
    path('ChatGPT_helper/forms_output/', forms_output, name='forms_output'),
    # Путь к странице с ответом:
    path('ChatGPT_helper/view_answer/', view_answer, name='view_answer'),
    # Путь для обновления ответа:
    path('ChatGPT_helper/update_answer/', update_answer, name='update_answer')
]
