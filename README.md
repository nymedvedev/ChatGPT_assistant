<a name="readme-top"></a>
<div align="center">
  <h1>ChatGPT-assistant</h1>
  <a href="https://github.com/nymedvedev/ChatGPT_assistant.git">
    <img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/chatgpt_assistant_logo.png?raw=true" alt="Logo" width="960" height="230">
  </a>
  <br />
  <p>
    <br />
    Мой сайт, на котором можно отправлять запросы в ChatGPT от OpenAI и получать ответы. <br />
    Рабочее название: <b>ChatGPT-helper</b>.<br />
     <br />
    <br />
    My site, where you can send requests to ChatGPT (OpenAI) and receive responses.<br />
    Working title: <b>ChatGPT-helper</b>.
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## О проекте / About The Project
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Authorization.png?raw=true" alt="Authorization page"><br />
В рамках своего первого рабочего проекта я сделал сайт, связанный с **ChatGPT** от **OpenAI** через **API Assistant**.<br />
На главной странице сайта - **форма авторизации**, либо вы можете нажать кнопку "**Регистрация**". <br />
<br />
As part of my first working project, I made a website related to ChatGPT from OpenAI via the API Assistant.<br />
There is an authorization form on the main page of the site, or you can click the "Register" button.<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Registration.png?raw=true" alt="Registration page"><br />
На странице регистрации требуется ввести вашу **эл. почту** и придумать **пароль** для входа. <br />
После регистрации страница обновится, вам нужно будет авторизоваться и вы попадёте на страницу с формой отправки запросов в **ChatGPT**.<br />
<br />

On the registration page, you need to enter your email address and come up with a password to log in.<br />
After registration, the page will be updated, you will log in and get to the page with the form for sending requests to ChatGPT.<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Form%20request.png?raw=true" alt="Form request page"><br />
Страница отправки запросов выглядит следующим образом.<br />
<br />
The request submission page looks like this.<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Response%20with%20serials.png?raw=true" alt="Response page"><br />
После отправки запроса страница обновится и вы окажетесь на странице с формой вывода ответа. Тут же можно отправить **следующий запрос**.
В данном примере был направлен запрос "**_Напиши 5 отличных сериалов._**"<br />
<br />
After sending the request, the page will be updated and you will find yourself on a page with a response output form. You can immediately send the following request.
In this case, the request was sent "Write 5 great TV series."<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Response%20with%20code.png?raw=true" alt="Response page"><br />
В данном примере был направлен запрос "**_Напиши калькулятор на Python._**" Форма вывода идентифицирует код и формирует вывод кода с подсветкой синтаксиса.<br />
Корректно выводится код любого языка программирования: Python, JavaScript, Ruby, C++, Java и т.д. (за это отвечает соотв. функция моего проекта)<br />
<br />
In this example, the request was sent "Write a calculator in Python." The output form identifies the code and generates code output with syntax highlighting.<br />
The code of any Programming language is displayed correctly: Python, JavaScript, Ruby, C++, Java, etc. (responsible for this is the corresponding my project's function)<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/Response%20with%20recipes.png?raw=true" alt="Response page"><br />
В данном примере был направлен запрос "**_Напиши 2 рецепта бургеров_.**". Информация ответа, содержащая списки и подпункты, выводится аккуратно упорядоченной. (за это отвечает соотв. функция моего проекта)<br />
<br />
In this example, the request "Write 2 burger recipes" was sent. The response information containing lists and sub-items is displayed in a neatly ordered manner. (responsible for this is the corresponding my project's function)<br />
<br />
<br />
<img src="https://github.com/nymedvedev/ChatGPT_assistant/blob/main/screenshots/MySQL%20DB.png?raw=true" alt="MySQL DB page">
Настроил сохранение текста запросов пользователей и текста ответов ChatGPT в **базу данных MySQL** на веб-сервере. С целью возможности в дальнейшем проанализировать данные и определить роли для **ChatGPT-ассистента**, которые можно будет выбрать зарегистрированному пользователю. Чтобы ChatGPT отвечал в определённой манере, либо подстраивался под конкретного пользователя с учётом специфики запросов.<br />
<br />
Configured saving the text of user requests and the text of ChatGPT responses to the MySQL database on the web server. In order to be able to further analyze the data and determine the roles for the ChatGPT assistant that can be selected by the registered user. So that ChatGPT responds in a certain manner, or adapts to a specific user.<br />
<br />
<br />
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Порядок разработки / The order of development
Проект разрабатывал в следующем порядке:
<ol>
  <li> Создал базовый проект на <b>Django</b>.</li>
  <br />
  <li> Подключился к удалённому рабочему пустому репозиторию на <b>GitHub</b>. <br />
          - Далее все обновления проекта отправлял в него. <br />
          - Проект в репозитории = проект на веб-сервере компании. <br />
          - Так я отслеживал поведение проекта не только на локальном сервере.<br />
    <br />
  <li> Создал на <b>HTML</b> (с <b>CSS</b>) шаблоны: </li>
          - страницы авторизации;<br />
          - страницы регистрации; <br />
          - форму отправки запросов; <br />
          - форму получения ответов.  <br />
            (Итого 4 HTML-файла, стили поместил внутрь.) <br />
  <br />
  <li> Создал приложение <b>users</b> для работы с блоком функций <b>авторизации</b> и <b>регистрации</b> пользователей.  <br />
          - В <b>users/urls</b> прописал пути 1) к странице авторизации (глав.стр.) и 2) регистрации.  <br />
          - Во <b>users/views</b> создал функцию для выполнения регистрации, которая делает редирект на стр. авторизации. <br />
          - В <b>users/models</b> создал класс профиля юзера с именем и емейлом. <br />
          - В <b>users/forms</b> создал классы для 1) авторизации и 2) регистрации. <br />
          - Добавил в HTML-документы авторизации и регистрации <b>шаблонные теги</b> Django для вывода полей авторизации и регистрации.<br />
    <br />
  <li> Создал приложение<b> forms </b>для работы с блоком функций <b>отправки запроса</b> в <b>ChatGPT</b> и <b>получения ответов</b>. </li>
  <br />
          - В <b>forms/urls</b> прописал пути: <br />
                    1) к странице с <b>первоначальным</b> запросом; <br />
                    2) путь для перехода к форме с <b>ответом</b>, делает редирект на стр. с ответом;  <br />
                    3) стр. с ответом и формой для <b>след. запроса</b>;   <br />
                    4) путь для обновл. ответа, делает обновл. стр. с выводом <b>нов. ответа</b>; <br />
  <br />
          - В <b>forms/forms</b> создал класс для отправки <b>запроса</b>;<br />
  <br />
          - Во <b>forms/views</b> создал следующие функции: <br />
                    1) Асинхронная функция для обращения к ChatGPT через<b> API</b>; <br />
                    2) Ас. ф. для обработки <b>HTTP-запроса</b> и отображения <b>формы</b> запроса на сайте;  <br />
                    3) Ас. ф. обрабатывающая <b>запросы</b>, отправленные через форму на сайте, выполняющая запросы к <b>ChatGPT</b> и выполняющая <b>редирект</b>; <br />
                    4) Ф. для отображения страницы с <b>ответом</b>; <br />
                    5) Ас. ф. для отображения <b>нового ответа</b> на странице; <br />
                    6) Ac. ф., к-ая отвечает за обработку <b>AJAX-запросов</b> с формы на странице.<br />
                    (Когда пользователь вводит новый запрос в форму и отправляет его,
                      AJAX-запрос отправляется на сервер, и именно эта функция обрабатывает этот запрос)<br />
                    7) Ф., которая, если в тексте ответа есть <b>код</b>, подсвечивает и форматирует его для вывода, как в <b>IDE</b>.<br />
  <br />
              Также, помимо описанного, ф-ции в <b>views</b> решают такие задачи, как: <br />
                      > получание <b>API KEY</b> из внешнего окружения с исп. библиотеки <b>dotenv</b>;<br />
                      > получение, преобразование и хранение данных <b>сессии</b>;<br />
                      > сохранение отдельных данных запроса в таблицу в <b>БД MySQL</b> веб-сервера на осн. phpMyAdmin (вместо исп. стандартной БД SQLite3);<br />
  <br />
          - В <b>forms/models</b> создал класс, представл. собой модель таблицы с нужными для сохранения столбцами данных. <br />
              (сохраняем необх. данные запроса-ответа в БД для аналитики) <br />
  <br />
          - В <b>forms/apps</b> создал класс для определением конфигурации прил. forms;<br />
  <br />
          - Добавил в HTML-документ формы отправки запроса <b>шаблонный тег</b> Django для отобр. поля отправки запроса;<br />
  <br />
          - Добавил в HTML-документ формы вывода ответа <b>шаблонный тег</b> Django с <b>Java-Script</b>-скриптом для отобр. ответа с учётом форматирования текста выводимого ответа;<br />
  <br />
     <li> Спрятал Secret Key Django-проекта и пароль от БД MySQL во внешнем окружении.</b> </li>     
</ol>
<br />
<br />
В настоящее время проект находится в работе, о новых функциях сообщу здесь дополнительно!<br />
<br />
<br />
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Разработал с помощью / Built With


* [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)][Python-url]
* [![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)][Django-url]
* [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)][HTML-url]
* [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)][CSS-url]


<!-- CONTACT -->
## Контакт / Contact

Nikolay Medvedev - Telegram: @ny_medvedev - medvedev.ny@gmail.com

Project Link: [https://github.com/nymedvedev/ChatGPT_assistant](https://github.com/nymedvedev/ChatGPT_assistant)


[Python-url]: https://www.python.org
[Django-url]: https://www.djangoproject.com/
[HTML-url]: https://html.com/html5/
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html


## [Лицензия / License](https://github.com/nymedvedev/ChatGPT_assistant/blob/main/LICENSE.md)

<b>ChatGPT_assistant</b> © [Medvedev Nikolay](https://github.com/nymedvedev)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


