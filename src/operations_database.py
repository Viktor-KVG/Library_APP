from src.book_validator import BookValidator
from src.db_connection import DBConnection

"""Класс с основными операциями в библиотеке"""
class OperationsDataBase(DBConnection, BookValidator):
    def __init__(self):
        super().__init__()  # Инициализируем родительский класс

    def create_book(self):
        """Добавляет новую книгу в базу данных."""
        existing_data = self.data  # Если файл не существует, создаем пустой список
        #проверка на выход, что при вводе exit возвращает None
        title = self.get_book_title()
        if title is None:
            return None

        author = self.get_book_author()
        if author is None:
            return None

        year = self.get_book_year()
        if year is None:
            return None

        new_data = {
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии',
        }

        new_data['id'] = self.get_unique_id()
        existing_data.append(new_data)
        self.write_db(existing_data)
        print("Книга успешно добавлена:", new_data)

    def del_book(self):
        """Удаляет книгу из базы данных по ID значению."""
        id_data = self.get_book_by_id()

        if id_data:
            book_exist = [exist for exist in self.data if id_data == exist['id']]
            if book_exist:
                new_list = [book for book in self.data if id_data != book['id']]
                self.write_db(new_list)
                print('Книга была успешно удалена')
            else:
                print('Значение не найдено или не корректно')

    def search_book(self):
        """Поиск книги по названию, автору и году выпуска"""
        title = self.get_book_title()
        if title is None:
            return None

        author = self.get_book_author()
        if author is None:
            return None

        year = self.get_book_year()
        if year is None:
            return None

        search_request = [book for book in self.data if title == book['title']
                          or year == book['year'] or author == book['author']]
        first_response = search_request[0]
        if first_response:
            print(f'Наиболее подходящий ответ на ваш запрос: ID:{first_response['id']}, Title: '
                  f'{first_response['title']}, Author: {first_response['author']}, '
                      f'Year: {first_response['year']}, Status: {first_response['status']}')
        else:
            print('Книга не найдена')

    def show_all_books(self):
        """Выводит список всех книг, которые есть в наличии"""
        if self.data:
            for book in self.data:
                print(f'ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, '
                      f'Year: {book['year']}, Status: {book['status']}')
        else:
            print('В библиотеке нет ни одной книги')

    def update_status(self):
        """Выполняет обновление статуса книги"""
        id_data = self.get_book_by_id()
        book_exist = [exist for exist in self.data if id_data == exist['id']]

        if book_exist:
            book_exist = book_exist[0]
            value = self.get_status_change()
            book_exist['status'] = value
            print('Статус книги обновлён')
            self.write_db(self.data)
        else:
            print('Значение не найдено или не корректно')