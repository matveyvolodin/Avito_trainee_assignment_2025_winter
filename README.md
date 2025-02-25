# Структура проекта

## Task_1
- **Task_1** – Файл *.pdf с описанием багов Задания 1.

## Task_2
- **BUGS.md** - Описание багов задания 2.
- **components.py** – Описанные компоненты тестов.
- **conftest.py** – Фикстуры для тестов.
- **data.py** – URL и некоторые данные для тестов.
- **pytest.ini** – Параметры запуска тестов (`--headed`).
- **TESTCASES.md** - Тесткейсы для Задания 2.
- **test_task2.py** – Тесты для Задания 2.

## Корневые файлы
- **.gitignore** - Директории, которые должны игнорироваться гитом.
- **requirements.txt** – Необходимые зависимости для работы тестов.
- **README.md** – Файл с описанием структуры проекта и инструкцией по локальному запуску.

# Инструкция по локальному запуску тестов

1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале: <br>
```git clone https://github.com/matveyvolodin/Avito_trainee_assignment_2025_winter```

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду: <br>
```python -v```  
Если он не установлен, то установите с официального сайта Python, выбрав подходящую версию для вашей операционной
системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH".

3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду: <br>
```cd ``` (здесь укажите путь до директории с проектом) 
4. Установите необходимые зависимости из файла requirements.txt, выполнив команду: </br>
```pip install -r requirements.txt  ```
если она не выполняется, то попробуйте:
```pip3 install -r requirements.txt  ```

5. После выполнения предыдущего пункта при необходимости установите файлы браузера, выполнив команду: <br>
```playwright install chrome ``` 

6. Запустите тесты, выполнив команду: <br>
```pytest -v```  
