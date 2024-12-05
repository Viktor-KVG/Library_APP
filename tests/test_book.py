import unittest
from io import StringIO
from unittest.mock import patch

from src.book_validator import BookValidator


"""Класс тестирует ввод неверных данных для полей книги"""

class TestBookValidator(unittest.TestCase):
    """Ввод неверных данных в поле title"""
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
        """Ввод неверных данных в поле author"""
        result = BookValidator.get_book_author()

        self.assertIsNone(result)

        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)# Для пустого ввода
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)  # Для ввода чисел
        self.assertIn('Поле автор должно содержать от 1 до 40 символов и состоять только из букв.', output)  # Для длинного ввода
        self.assertIn('Выход из программы...', output)  # Сообщение об выходе


    @patch('builtins.input', side_effect=['', '12345', '2025', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_book_year(self, mock_stdout, mock_input):
        """Ввод неверных данных в поле year"""
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