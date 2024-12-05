import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from src.main import BookValidator, OperationsDataBase, PATH_DB

# PATH_TEST_DB = 'home/vitass/Desktop/library_app/pythonProject/tests/test_db.json'
class TestBookValidator(unittest.TestCase):
    # PATH_DB = 'home/vitass/Desktop/library_app/pythonProject/tests/test_db.json'



    # @patch('builtins.input', side_effect=['', 'Valid Book Title'])
    # def test_get_book_title_empty(self, mock_input):
    #     title = BookValidator.get_book_title()
    #     self.assertEqual(title, 'Valid Book Title')
    #
    # @patch('builtins.input', side_effect=['Invalid Title' * 10, 'Valid Title'])
    # def test_get_book_title_too_long(self, mock_input):
    #     """Тестируем метод get_book_title на слишком длинном вводе"""
    #     title = BookValidator.get_book_title()
    #     self.assertEqual(title, 'Valid Title')
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_book_title_exit(self, mock_input):
    #     """Тестируем метод get_book_title на вводе 'exit'"""
    #     title = BookValidator.get_book_title()
    #     self.assertIsNone(title)
    #
    #
    # @patch('builtins.input', side_effect=['', 'Valid Author'])
    # def test_get_book_author_empty(self, mock_input):
    #     author = BookValidator.get_book_author()
    #     self.assertEqual(author, 'Valid Author')
    #
    # @patch('builtins.input', side_effect=['Invalid123', 'Valid Author'])
    # def test_get_book_author_invalid_characters(self, mock_input):
    #     author = BookValidator.get_book_author()
    #     self.assertEqual(author, 'Valid Author')
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_book_author_exit(self, mock_input):
    #     """Тестируем метод get_book_author на вводе 'exit'"""
    #     author = BookValidator.get_book_author()
    #     self.assertIsNone(author)
    #
    # @patch('builtins.input', side_effect=['2025', '2023'])
    # def test_get_book_year_invalid(self, mock_input):
    #     year = BookValidator.get_book_year()
    #     self.assertEqual(year, 2023)  # Убедитесь, что ваша функция возвращает целое число
    #
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_book_year_exit(self, mock_input):
    #     """Тестируем метод get_book_year на вводе 'exit'"""
    #     year = BookValidator.get_book_year()
    #     self.assertIsNone(year)
    #
    # @patch('builtins.input', side_effect=['abc', '1'])
    # def test_get_book_by_id_invalid(self, mock_input):
    #     """Тестируем метод get_book_by_id на вводе недопустимого ID"""
    #     id_data = BookValidator.get_book_by_id()
    #     self.assertEqual(id_data, 1)
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_book_by_id_exit(self, mock_input):
    #     """Тестируем метод get_book_by_id на вводе 'exit'"""
    #     id_data = BookValidator.get_book_by_id()
    #     self.assertIsNone(id_data)
    #
    # @patch('builtins.input', side_effect=['not a status', 'в наличии'])
    # def test_get_status_change_invalid(self, mock_input):
    #     """Тестируем метод get_status_change на вводе недопустимого статуса"""
    #     status = BookValidator.get_status_change()
    #     self.assertEqual(status, 'в наличии')
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_status_change_exit(self, mock_input):
    #     """Тестируем метод get_status_change на вводе 'exit'"""
    #     status = BookValidator.get_status_change()
    #     self.assertIsNone(status)
    #
    # @patch('builtins.input', side_effect=['7', '1'])
    # def test_get_safe_action_invalid(self, mock_input):
    #     """Тестируем метод get_safe_action на вводе недопустимого действия"""
    #     action = BookValidator.get_safe_action()
    #     self.assertEqual(action, '1')
    #
    # @patch('builtins.input', side_effect=['exit'])
    # def test_get_safe_action_exit(self, mock_input):
    #     """Тестируем метод get_safe_action на вводе 'exit'"""
    #     action = BookValidator.get_safe_action()
    #     self.assertIsNone(action)

    # def setUp(self):
    #     if os.path.exists(self.PATH_DB):
    #         os.remove(self.PATH_DB)

    # @patch('builtins.input', side_effect=['The Great Gatsby', 'F. Scott Fitzgerald', '2023'])
    # def test_create_book(self, mock_input):
    #     db = OperationsDataBase()
    #     db.data = []  # Инициализируем пустой список
    #     db.create_book()  # Создаем книгу
    #
    #     # Проверяем, что книга была добавлена
    #     with open(self.PATH_DB, 'r') as db_file:
    #         data = json.load(db_file)
    #
    #     self.assertEqual(len(data), 1)  # Ожидаем, что книга добавлена
    #     self.assertEqual(data[0]['title'], 'The Great Gatsby')  # Проверяем название
    #
    # @patch('builtins.input', side_effect=['1'])  # id книги для удаления
    # def test_del_book(self, mock_input):
    #     db = OperationsDataBase()
    #     db.data = [{'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': '2023',
    #                 'status': 'в наличии'}]
    #     db.write_db(db.data)  # Записываем данные в тестовый файл
    #     db.del_book()  # Удаляем книгу по ID
    #
    #     # Проверяем, что файл пустой после удаления
    #     with open(self.PATH_DB, 'r') as db_file:
    #         data = json.load(db_file)
    #
    #     self.assertEqual(data, [])  # Должен быть пустой список
    @patch('builtins.input', side_effect=['',  # Пустой ввод
                                            'Too long title that exceeds the maximum length of seventy characters, which is not acceptable.',  # Длинный ввод
                                            'exit'])  # Выход
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_book_title(self, mock_stdout, mock_input):
        # Получаем результат от метода get_book_title
        result = BookValidator.get_book_title()
        # Проверяем, что возвращаемое значение корректное
        self.assertIsNone(result)  # Ожидаем, что возвращает None после exit
        # Проверяем выводимые сообщения
        output = mock_stdout.getvalue().strip().split('\n')
        # Проверяем сообщения об ошибке и выходе
        self.assertIn('Поле книги является обязательным для заполнения и должно содержать от 1 до 70 символов.', output)  # Для пустого ввода
        self.assertIn('Поле книги является обязательным для заполнения и должно содержать от 1 до 70 символов.', output)  # Для длинного ввода
        self.assertIn('Выход из программы...', output)  # Сообщение об выходе



    @patch('builtins.input', side_effect=['',
                                            '12345',  # Неверный ввод (числа)
                                            'Too long author name that exceeds the maximum length of forty characters',  # Слишком длинный ввод
                                            'exit'])  # Выход
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_book_author(self, mock_stdout, mock_input):
        result = BookValidator.get_book_author()
        self.assertIsNone(result)
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)# Для пустого ввода
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)  # Для ввода чисел
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)  # Для длинного ввода
        self.assertIn('Выход из программы...', output)  # Сообщение об выходе

    @patch('builtins.input', side_effect=[
        '',  # Неверный ввод (пустая строка)
        '12345',  # Неверный ввод (числа)
        '2025',  # Неверный ввод (число больше 2024)
        'exit'  # Выход
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_book_year(self, mock_stdout, mock_input):
        # Выполняем функцию
        result = BookValidator.get_book_year()

        # Проверяем, что корректный год возвращается
        self.assertIsNone(result)  # Проверяем, что возвращается None при выходе

        # Получаем весь вывод
        output = mock_stdout.getvalue().strip().split('\n')

        # Проверяем наличие соответствующих сообщений в выводе
        self.assertIn('Поле year должно содержать 4 цифры и не превышать 2024.', output)  # Для пустого ввода
        self.assertIn('Поле year должно содержать 4 цифры и не превышать 2024.', output)  # Для ввода чисел
        self.assertIn('Поле year должно содержать 4 цифры и не превышать 2024.', output)  # Для числа больше 2024
        self.assertIn('Выход из программы...', output)  # Сообщение об выходе