
# Answers Project

Цей проект - веб-додаток, який дозволяє відповідати на питання, що можуть цікавити користувача за змістом PDF-файлів.

## Початок роботи

Нижче наведені кроки для встановлення та запуску проекту на вашому локальному комп'ютері.

### Передумови

Рекомендую використовувати віртуальне середовище для ізоляції залежностей. Також для запуску обробки pdf фалів необхідно встановити .net: https://dotnet.microsoft.com/en-us/download/dotnet/6.0

### Встановлення

1. Створіть віртуальне середовище:
    ```
    virtualenv venv
    venv\Scripts\activate
    ```

2. Встановіть необхідні пакети:
    ```
    pip install Django
    pip install ironpdf
    pip install --upgrade langchain-openai tiktoken chromadb langchain
    pip install langchainhub
    ```

3. Перейдіть до каталогу проекту:
    ```
    cd answers_project
    ```

4. Виконайте міграцію бази даних:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Налаштуйте ключі:
    - Змініть ключ `ironpdf` в файлі `answers_project\pdf\preprocess.py`
    - Змініть ключ `openai_api_key` в файлі `answers_project\chat\llm.py`

6. Запустіть сервер:
    ```
    python manage.py runserver
    ```

Після цих кроків проект буде доступний за адресою http://127.0.0.1:8000/.



