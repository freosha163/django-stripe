## С использованием докера:
#### 1. Выберите месо на жестком диске, где будет находиться проект

#### 2. Клонируйте репозиторий

    git clone https://github.com/freosha163/django-stripe

#### 3. Вставьте эти команды в терминал
Создаем контейнер

    docker-compose build

Запускаем проект

    docker-compose up

### Это все, что нужно для начала


## Запуск без Докера:
#### 1. Выберите место на жестком диске, где будет находиться проект

#### 2. Клонируйте репозиторий

    git clone https://github.com/freosha163/django-stripe

#### 3. В корне проекта запустите эту команду

    pip install -r requirements.txt

#### 4. После установки всех зависимостей напишите в терминал следующие команды:
    
    cd djangostripe 

    python manage.py migrate

    python manage.py runserver

### Это все, что нам нужно, для запуска без Докера