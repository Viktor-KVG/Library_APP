
import unittest
from unittest.mock import patch, MagicMock

from library_app.src.menu_navigator import MenuNavigator
from library_app.src.operations_database import OperationsDataBase


class TestBookOperations(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр класса
        self.operations_db = OperationsDataBase()
        # Инициализируем self.data с тестовыми данными
        self.operations_db.data = [
            {'id': 1, 'title': 'Книга 1', 'author': 'Автор Один', 'year': '2020', 'status': 'в наличии'},
            {'id': 2, 'title': 'Книга 2', 'author': 'Автор Два', 'year': '2021', 'status': 'выдана'},
        ]

        self.navigator = MenuNavigator()
        self.navigator.create_book = MagicMock()
        self.navigator.del_book = MagicMock()
        self.navigator.search_book = MagicMock()
        self.navigator.show_all_books = MagicMock()
        self.navigator.update_status = MagicMock()

    @patch('builtins.input', side_effect=['1'])  # Имитация ввода пользователя
    @patch.object(OperationsDataBase, 'write_db', return_value=None)  # Имитация метода write_db
    def test_del_book_success(self, mock_write_db, mock_input):
        """Тест успешного удаления книги по ID."""
        self.operations_db.del_book()
        # Проверяем, что книга была удалена
        self.assertEqual(len(self.operations_db.data), 1)
        self.assertEqual(self.operations_db.data[0]['id'], 2)
        mock_write_db.assert_called_once()  # Проверяем, что write_db был вызван

    @patch('builtins.input', side_effect=['3'])  # Имитация ввода пользователя
    @patch('builtins.print')  # Имитация print
    def test_del_book_not_found(self, mock_print, mock_input):
        """Тест на случай, если книга не найдена."""
        self.operations_db.del_book()
        mock_print.assert_called_with('Значение не найдено или не корректно')

    @patch('builtins.input', side_effect=['exit'])  # Имитация ввода пользователя
    def test_del_book_exit(self, mock_input):
        """Тест выхода из функции удаления книги."""
        result = self.operations_db.del_book()
        self.assertIsNone(result)  # Проверяем, что результат None, если введено 'exit'

    @patch('builtins.input', side_effect=['Книга 2', 'Автор Два', '2021'])  # Все три ввода
    @patch('builtins.print')
    def test_search_book_success(self, mock_print, mock_input):
        """Тест успешного поиска книги."""
        result = self.operations_db.search_book()

        expected_result = {'id': 2, 'title': 'Книга 2', 'author': 'Автор Два', 'year': '2021', 'status': 'выдана'}

        # Проверка, что вывод был правильным
        mock_print.assert_called_with(
            'Наиболее подходящий ответ на ваш запрос: ID: 2, Title: Книга 2, Author: Автор Два, Year: 2021, Status: выдана')

        # Проверка, что метод вернул правильный результат
        self.assertEqual(result, expected_result)

    @patch('builtins.input', side_effect=['Книга', 'Автор', '2023',])  # Все три ввода
    @patch('builtins.print')
    def test_search_book_not_found(self, mock_print, mock_input):
        """Тест, когда книга не найдена."""
        result = self.operations_db.search_book()

        # Проверка, что вывод был правильным
        mock_print.assert_called_with('Книга с такими критериями не найдена')

        # Проверка, что результат равен None
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['exit'])  # Один ввод для выхода
    @patch('builtins.print')
    def test_search_book_exit(self, mock_print, mock_input):
        """Тест выхода из метода поиска."""
        result = self.operations_db.search_book()

        # Проверка правильного выхода
        mock_print.assert_called_with('Выход в меню...')

        # Проверка, что результат равен None
        self.assertIsNone(result)

    @patch('builtins.print')  # Заменяет функцию print на mock
    def test_show_all_books_with_books(self, mock_print):
        """Тест показывает все книги в библиотеке."""
        self.operations_db.show_all_books()

        # Проверяем правильный вывод
        mock_print.assert_any_call('ID: 1, Title: Книга 1, Author: Автор Один, Year: 2020, Status: в наличии')
        mock_print.assert_any_call('ID: 2, Title: Книга 2, Author: Автор Два, Year: 2021, Status: выдана')

    @patch('builtins.print')
    def test_show_all_books_empty(self, mock_print):
        """Тест, когда в библиотеке нет книг."""
        self.operations_db.data = []  # Пустой список книг

        # Вызываем метод
        self.operations_db.show_all_books()

        # Проверяем правильный вывод
        mock_print.assert_called_with('В библиотеке нет ни одной книги')

    @patch('builtins.input', side_effect=['1', 'выдана'])  # Имитация ввода пользователя
    @patch('builtins.print')  # Имитация print
    def test_update_status_success(self, mock_print, mock_input):
        """Тест успешного обновления статуса книги по ID."""
        self.operations_db.get_book_by_id = MagicMock(return_value=1)  # Метод для возврата id 1
        result = self.operations_db.update_status()
        self.assertIsNone(result)  # Ожидаем None, так как обновление прошло успешно
        mock_print.assert_called_with('Статус книги обновлён')  # Проверяем, что выводится правильное сообщение

    @patch('builtins.input', side_effect=['3', 'выдана'])  # Имитация ввода пользователя
    @patch('builtins.print')  # Имитация print
    def test_update_status_book_not_found(self, mock_print, mock_input):
        """Тест на случай, если книга не найдена."""
        self.operations_db.get_book_by_id = MagicMock(return_value=None)  # Метод для возврата None, книги нет
        result = self.operations_db.update_status()
        self.assertIsNone(result)  # Ожидаем None, так как книги нет в базе
        mock_print.assert_called_with('Значение не найдено или не корректно')  # Проверяем сообщение об ошибке

    @patch('builtins.input', side_effect=['exit'])  # Имитация ввода пользователя
    def test_update_status_exit(self, mock_input):
        """Тест на случай, если пользователь вводит 'exit'."""
        result = self.operations_db.update_status()
        self.assertIsNone(result)  # Ожидаем None, так как пользователь вышел

    @patch('builtins.input', side_effect=['6'])  # Имитация ввода '6' для выхода
    def test_actions_exit(self, mock_input):
        result = self.navigator.actions()
        self.assertIsNone(result)  # Ожидаем, что вернется None
        # проверяем, что методы ниже н были вызваны при вводе '6'
        self.navigator.create_book.assert_not_called()
        self.navigator.del_book.assert_not_called()
        self.navigator.search_book.assert_not_called()
        self.navigator.show_all_books.assert_not_called()
        self.navigator.update_status.assert_not_called()

    @patch('builtins.input', side_effect=['1'])  # Имитация ввода '1' для создания книги
    def test_actions_create_book(self, mock_input):
        result = self.navigator.actions()
        self.assertTrue(result)  # Ожидаем, что вернется True
        # проверяем, что методы ниже не были вызваны при вводе '1'
        self.navigator.create_book.assert_called_once()
        self.navigator.del_book.assert_not_called()
        self.navigator.search_book.assert_not_called()
        self.navigator.show_all_books.assert_not_called()
        self.navigator.update_status.assert_not_called()

    @patch('builtins.input', side_effect=['2'])  # Имитация ввода '2' для удаления книги
    def test_actions_delete_book(self, mock_input):
        result = self.navigator.actions()
        self.assertTrue(result)  # Ожидаем, что вернется True
        self.navigator.del_book.assert_called_once()
        self.navigator.create_book.assert_not_called()
        self.navigator.search_book.assert_not_called()
        self.navigator.show_all_books.assert_not_called()
        self.navigator.update_status.assert_not_called()

    @patch('builtins.input', side_effect=['3'])  # Имитация ввода '3' для поиска книги
    def test_actions_search_book(self, mock_input):
        result = self.navigator.actions()
        self.assertTrue(result)  # Ожидаем, что вернется True
        self.navigator.search_book.assert_called_once()
        self.navigator.create_book.assert_not_called()
        self.navigator.del_book.assert_not_called()
        self.navigator.show_all_books.assert_not_called()
        self.navigator.update_status.assert_not_called()

    @patch('builtins.input', side_effect=['4'])  # Имитация ввода '4' для показа всех книг
    def test_actions_show_all_books(self, mock_input):
        result = self.navigator.actions()
        self.assertTrue(result)  # Ожидаем, что вернется True
        self.navigator.show_all_books.assert_called_once()
        self.navigator.create_book.assert_not_called()
        self.navigator.del_book.assert_not_called()
        self.navigator.search_book.assert_not_called()
        self.navigator.update_status.assert_not_called()

    @patch('builtins.input', side_effect=['5'])  # Имитация ввода '5' для обновления статуса
    def test_actions_update_status(self, mock_input):
        result = self.navigator.actions()
        self.assertTrue(result)  # Ожидаем, что вернется True
        self.navigator.update_status.assert_called_once()
        self.navigator.create_book.assert_not_called()
        self.navigator.del_book.assert_not_called()
        self.navigator.search_book.assert_not_called()
        self.navigator.show_all_books.assert_not_called()