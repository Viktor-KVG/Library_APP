
"""Класс для проверки ошибок при вводе"""
class BookValidator:
    @staticmethod
    def get_book_title():
        """Запрашивает название книги и проверяет его корректность."""
        while True:
            title = input('Введите название книги (1-70 символов): ')
            if title.lower() == 'exit':
                print('Выход в меню...')
                return None
            if len(title) < 1 or len(title) > 70:
                print('Поле книги является обязательным для заполнения и должно содержать от 1 до 70 символов.')
                continue
            return title

    @staticmethod
    def get_book_author():
        """Запрашивает имя автора и проверяет его корректность."""
        while True:
            author = input('Введите автора книги (1-40 символов): ')
            if author.lower() == 'exit':
                print('Выход в меню...')
                return None
            if len(author) < 1 or len(author) > 40 or not all(c.isalpha() or c.isspace() for c in author):
                print('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.')
                continue
            return author.title()

    @staticmethod
    def get_book_year():
        """Запрашивает год выпуска книги и проверяет его корректность."""
        while True:
            year = input('Введите год выпуска книги (4 цифры, не более 2024): ')
            if year.lower() == 'exit':
                print('Выход в меню...')
                return None  # Завершаем выполнение
            if len(year) != 4 or not year.isdigit() or int(year) > 2024:
                print('Поле year должно содержать 4 цифры и не превышать 2024.')
                continue  # Продолжаем запрашивать год
            return year  # Ввод корректен, возвращаем год

    @staticmethod
    def get_book_by_id():
        """Запрашивает ID книги и проверяет его на корректность."""
        while True:
            id_data = input('Введите ID книги (число):')
            if id_data.lower() == 'exit':
                print('Выход в меню...')
                return None
            if not id_data.isdigit():
                print('Поле ID должно иметь числовое значение')
                continue
            return int(id_data)

    @staticmethod
    def get_status_change():
        """Запрашивает ID книги и проверяет его на корректность."""
        right_value = ['в наличии', 'выдана']
        while True:
            data = input('Введите статус книги:')
            if data.lower() == 'exit':
                print('Выход в меню...')
                return None
            if data not in right_value:
                print(f'Можно ввести только одно из этих значений - {right_value}')
                continue
            return data

    @staticmethod
    def get_safe_action():
        """Запрашивает ID книги и проверяет его на корректность."""
        right_value = ['1', '2', '3', '4', '5', '6']
        while True:
            data = input('Введите желаемое действие в библиотеке по цифре:\n'
                     '1. Внести книгу\n'
                     '2. Удалить книгу\n'
                     '3. Найти книгу\n'
                     '4. Показать все книги\n'
                     '5. Обновить статус\n'
                     '6. Покинуть библиотеку\n'
                      )
            if data.lower() == 'exit' or data == '6':
                print('Выход из программы...')
                return None
            if not data.isdigit() or data not in right_value:
                print(f'Можно ввести только одно из этих значений - {right_value}')
                continue
            return data
