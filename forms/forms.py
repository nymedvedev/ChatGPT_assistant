from django import forms


# определяю форму для обработки данных со страницы ChatGPT-помощника:
class RequestForm(forms.Form):
    request = forms.CharField(widget=forms.Textarea(
        attrs={'maxlength': '10000', 'placeholder': 'Введите Ваш запрос и подождите несколько секунд'}), required=True
    )
