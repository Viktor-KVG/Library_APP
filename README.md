
#Название проекта: Library app

#Приложение включает следующие основные функции:

- **Добавление книги**: Позволяет пользователю добавить новую книгу с указанием названия, автора, года выпуска и статуса.
- **Удаление книги**: Удаляет книгу из базы данных по ее уникальному ID.
- **Поиск книги**: Позволяет искать книги по названию, автору и году выпуска.
- **Показ всех книг**: Выводит список всех книг, которые есть в наличии.
- **Обновление статуса книги**: Обновляет статус книги (например, "в наличии" или "выдана").

# Структура проекта
- `db/` - файл с базой данных
- `documentation/` - документация проекта.
- `src/` - файлы миграций/ревизий проекта.
  - `book_validator.py/` - файл с валидацией входных данных
  - `constatnts.py/` - файл с константными значениями
  - `db_conection.py` - файл с операциями обращения в базу данных.
  - `menu_navigator.py` - файл запуска меню приложения.
  - `operations_database.py` - файл с эндпоинтами к БД.
- `tests/` - файлы с тестированием функций
  - `test_book.py` - тестирование валидности входных данных.
- `main.py` - файл с запуском приложения
- `README.MD` - описание проекта.

##Перред использованием отредактируйте путь к файлу в 'constatnts.py'

# Использование

    Запустите приложение:

    python main.py

    (где main.py — это ваш файл, который запускает приложение)

    Следуйте инструкциям на экране для выполнения различных действий в библиотеке.

    Чтобы выйти из приложения, введите exit в любом месте, где требуется ввод.
    
## Пример использования

### Добавление книги
1. Выберите действие: `1` (для добавления книги)
2. Введите название книги: `Мастер и Маргарита`
3. Введите автора книги: `Булгаков`
4. Введите год выпуска книги: `1967`
5. Сообщение: `Книга успешно добавлена`

### Удаление книги
1. Выберите действие: `2` (для удаления книги)
2. Введите ID книги: `3` (предположим, что ID книги, которую вы хотите удалить, равен 3)
3. Сообщение: `Книга была успешно удалена`

### Поиск книги
1. Выберите действие: `3` (для поиска книги)
2. Введите название книги: `1984`
3. Введите автора книги: `Джордж Оруэлл`
4. Введите год выпуска книги: `1949`
5. Сообщение: `Наиболее подходящий ответ на ваш запрос: ID: 2, Title: 1984, Author: Джордж Оруэлл, Year: 1949, Status: в наличии`

### Показ всех книг
1. Выберите действие: `4` (для показа всех книг)
2. Сообщение: 

ID: 1, Title: Мастер и Маргарита, Author: Булгаков, Year: 1967, Status: в наличии
ID: 2, Title: 1984, Author: Джордж Оруэлл, Year: 1949, Status: в наличии


### Обновление статуса книги
1. Выберите действие: `5` (для обновления статуса книги)
2. Введите ID книги: `1` (предположим, что вы хотите обновить статус книги с ID 1)
3. Введите новый статус книги: `выдана`
4. Сообщение: `Статус книги обновлён`

### Выход из приложения
1. В любой момент введите `exit`, чтобы выйти в меню.
2. Выберите действие: `6` (для выхода из приложения)

    




