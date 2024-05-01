# всё это вьюха (отдельными функциями) для обработки формы
# и отправки запроса к ChatGPT через OpenAI API:

# импортируем модуль os, который предоставляет функции для взаимодействия с операционной системой:
import os
# импортируем модуль openai, который предоставляет функции для работы с OpenAI API:
import openai
# имп-м ф-ции для обраб. HTTP-запросов и форм-ния HTTP-ответов:
from django.shortcuts import render, redirect
# импортируем класс RequestForm для валидации данных, отправленных через форму на сайте:
from forms.forms import RequestForm
# импортируем класс PermissionDenied - это исключение для сигнализации о том, что у пользователя
# нет прав для выполнения определенного действия:
from django.core.exceptions import PermissionDenied
# Эта функция используется для чтения переменных окружения из файла .env:
from dotenv import load_dotenv
# Эта функция предоставляет доступ к кэшу Django:
from django.core.cache import caches
# Эта функция используется для преобразования синхронных функций в асинхронные:
from asgiref.sync import sync_to_async
# импортируем класс AsyncOpenAI -предст-ет асинхронный интерфейс для работы с OpenAI API:
from openai import AsyncOpenAI
# Этот класс используется для формирования HTTP-ответа в формате JSON:
from django.http import JsonResponse
# Эта функция выводит сообщение об ошибке:
from django.contrib import messages
# Библиотеки для стилей отображения ответа:
import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
# Библиотека для исп. регулярн. выражений:
import re
# импортирую модели для раб. c данными табл. StandaloneTraffic:
from forms.models import StandaloneTraffic
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime


# устанавливаю библиотеку python-dotenv ( pip install python-dotenv )
# устанавливаю переменную окружения: API-ключ от OpenAI из файла .env (не допущен в репозиторий).
# вызываю функцию load_dotenv для чтения переменных окружения из файла .env:
load_dotenv()
# получаю значение переменной окружения OPENAI_API_KEY с помощью функции os.getenv:
openai_api_key = os.getenv("OPENAI_API_KEY")
# устанавливаю значение переменной openai.api_key равным значению переменной openai_api_key:
openai.api_key = openai_api_key


def highlight_code(code_language, code_content):
    """ Если в тексте ответа есть КОД - эта функция его форматирует. """
    # Создает форматировщик HTML для вывода подсвеченного кода.
    # Параметры 1) linenos=False, 2) full=True, 3) style='native'\'zenburn' указывают на то,
    # что нужно 1) скрыть номера строк, 2) включить полный набор стилей и 3) использовать 'нативный' стиль:
    formatter = HtmlFormatter(linenos=False, style='zenburn')
    # Получает лексер (анализатор) для указанного языка программирования.
    # Параметр stripall=True указывает на то, что нужно удалить все классы из кода:
    lexer = get_lexer_by_name(code_language, stripall=True)
    # Применяет подсветку синтаксиса к коду:
    highlighted_code = highlight(code_content, lexer, formatter)
    # заменяем начальный тег <div class="highlight"><pre> на <pre>.
    # Это нужно для удаления лишнего тега <div>, который добавляется при создании форматировщика HTML:
    highlighted_code = highlighted_code.replace('<div class="highlight"><pre>', '<pre>')
    # заменяем конечный тег </pre></div> на </pre>.
    # Это нужно для удаления лишнего тега <div>, который добавляется при создании форматировщика HTML:
    highlighted_code = highlighted_code.replace('</pre></div>', '</pre>')
    # возвращаем отформатированный код с подсветкой синтаксиса:
    return highlighted_code


async def create_chat_completion(user_request, request_history, answer_history):
    async with AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY")) as client:
        try:
            print(f"Request history: {request_history}")
            print(f"Answer history: {answer_history}")
            messages = []
            for request, response in zip(request_history, answer_history):
                messages.append({"role": "user", "content": request})
                messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": user_request})
            # Добавляем текущий запрос

            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            content = response.choices[0].message.content
            html_content = markdown.markdown(content, extensions=['nl2br', 'fenced_code'])
            # Приведенная ниже обработка HTML может быть адаптирована под ваш конкретный случай
            html_content = html_content.replace('<div class="answer_content">', '<div class="answer_content"><ol>', 1)
            html_content = re.sub(r'<ol>\s*<li>(.*?):</li>\s*<li>(.*?)</li>', r'<li>\1:</li><ol><li>\2</li>', html_content)
            html_content = re.sub(r'<ol>\s*<li>(.*?)</li>', r'<li>\1</li>', html_content)
            html_content = html_content.replace('</div>', '</ol></div>', 1)
            return html_content
        except Exception as e:
            print(f"OpenAI API error: {e}")
            raise PermissionDenied("OpenAI API returned an error.")


async def request_form(request):
    """  Функция для обработки HTTP-запроса и отображения формы запроса на сайте """
    # Создает экземпляр класса RequestForm, определенного в файле forms.py.
    # Этот класс содержит информацию о полях формы и правилах их валидации.
    form = RequestForm()
    # Возвращает HTTP-ответ, сформированный функцией render.
    # Эта функция объединяет запрос request, шаблон form/form.html и контекст {"form": form}
    # для формирования HTML-страницы. Контекст содержит объект формы form, который будет доступен в шаблоне.
    return render(request, "form/form.html", {"form": form})


async def forms_output(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            user_request = form.cleaned_data['request']
            # Получаем или инициализируем историю запросов и ответов
            get_session_data = sync_to_async(request.session.get)
            request_history = await get_session_data('request_history', []) if await get_session_data('request_history', []) else []
            answer_history = await get_session_data('answer_history', []) if await get_session_data('answer_history', []) else []

            try:
                # Добавляем текущий запрос к истории запросов
                #request_history[len(request_history) + 1] = user_request
                request_history.append(user_request)
                await sync_to_async(request.session.__setitem__)('request_history', request_history)

                chat_completion = await create_chat_completion(user_request, request_history, answer_history)
                answer = chat_completion
                #answer_history[len(answer_history) + 1] = answer

                answer_history.append(answer)
                await sync_to_async(request.session.__setitem__)('answer_history', answer_history)

                await sync_to_async(request.session.save)()
                await sync_to_async(request.session.__setitem__)('answer_html', answer)

                username = await sync_to_async(lambda:request.user.username)()
                standalone_traffic = StandaloneTraffic(
                    timestamp=timezone.now(),
                    username=username,
                    request=str(user_request),
                    response=str(answer)
                )
                await sync_to_async(standalone_traffic.save)()

                return redirect('view_answer')
            except PermissionDenied as e:
                messages.error(request, str(e))
            else:
                form = RequestForm()
            return render(request, 'form/form.html', {'form': form})


# Получает объект кэша по умолчанию из подсистемы кэширования Django.
# Этот объект будет использоваться для доступа к кэшированным данным:
cache = caches['default']
# Преобразует синхронную функцию cache.get в асинхронную с помощью sync_to_async
# и сохраняет ее в переменной get_session.
# Эта функция будет использоваться для асинхронного получения данных из кэша:
get_session = sync_to_async(cache.get)
# Преобразует синхронную функцию cache.set в асинхронную с помощью sync_to_async
# и сохраняет ее в переменной set_session.
# Эта функция будет использоваться для асинхронного сохранения данных в кэше:
set_session = sync_to_async(cache.set)



def view_answer(request):
    """ Функция для отображения страницы с ответом. """
    # Создаем экземпляр формы RequestForm с данными POST-запроса:
    form = RequestForm(request.POST)
    # Получаем ответ из сессии.
    # Если ответ не найден, устанавливаем значение по умолчанию: "К сожалению, ответ не найден":
    answer_html = request.session.get("answer_html", "К сожалению, ответ не найден.")
    # Возвращаем HTML-шаблон "form/form_output.html" с контекстом, содержащим ответ и форму.
    return render(request, "form/form_output.html", {"answer": answer_html, "form": form})


async def update_answer(request):
    """ Функция для отображения нового ответа на странице. """
    #  Проверяем, является ли запрос POST-запросом и был ли он отправлен с помощью AJAX:
    # (AJAX = Asynchronous JavaScript and XML)
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Создаем экземпляр формы RequestForm с данными POST-запроса:
        form = RequestForm(request.POST)
        if form.is_valid():
            user_request = form.cleaned_data['request']
            # Получаем или инициализируем историю запросов и ответов
            get_session_data = sync_to_async(request.session.get)
            request_history = await get_session_data('request_history') if await get_session_data(
                'request_history') else []
            answer_history = await get_session_data('answer_history') if await get_session_data(
                'answer_history') else []
            try:
                # Вызываем асинхронную функцию create_chat_completion для получения ответа от ChatGPT:
                chat_completion = await create_chat_completion(user_request, request_history, answer_history)
                # Извлекаем содержимое ответа из объекта chat_completion:
                answer = chat_completion
                # Обновляем историю запросов и ответов
                request_history.append(user_request)
                answer_history.append(answer)
                await sync_to_async(request.session.__setitem__)('request_history', request_history)
                await sync_to_async(request.session.__setitem__)('answer_history', answer_history)

                # Асинхронно сохраняем ответ в сессии:
                await sync_to_async(request.session.__setitem__)('answer_html', answer)

                username = await sync_to_async(lambda: request.user.username)()
                # Сохраняем запрос и ответ в StandaloneTraffic
                standalone_traffic = StandaloneTraffic(
                    timestamp=timezone.now(),
                    username=username,
                    request=str(user_request),
                    response=str(answer)
                )
                await sync_to_async(standalone_traffic.save)()

                #  Возвращаем JSON-ответ с новым ответом:
                return JsonResponse({'answer': answer})
            # Перехватывает исключение PermissionDenied и возвращает JSON-ответ с ошибкой:
            except PermissionDenied as e:
                return JsonResponse({'error': str(e)})
    # Возвращает JSON-ответ с ошибкой, если запрос не валиден:
    return JsonResponse({'error': 'Invalid request'})


async def process_update_answer(request):
    """ Отвечает за обработку AJAX-запросов с формы на странице.
    Когда пользователь вводит новый запрос в форму и отправляет его,
    AJAX-запрос отправляется на сервер, и именно эта функция обрабатывает этот запрос.
    Комментарии аналогичны функции async def update_answer(request)"""
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = RequestForm(request.POST)
        if form.is_valid():
            user_request = form.cleaned_data['request']
            # Получаем или инициализируем историю запросов и ответов
            request_history = request.session.get('request_history', [])
            answer_history = request.session.get('answer_history', [])
            try:
                chat_completion = await create_chat_completion(user_request, request_history, answer_history)
                answer = chat_completion
                await sync_to_async(request.session.__setitem__)('answer', answer)
                return JsonResponse({'answer': answer})
            except PermissionDenied as e:
                return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request'})
