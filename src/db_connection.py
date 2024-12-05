import json

from src.constants import PATH_DB

"""Класс для взаимодействия с базой данных"""
class DBConnection:
    def __init__(self):
        self.data = self.read_db()  # Загружаем данные при инициализации
        self.index = 0  # Индекс для итерации

    @staticmethod
    def read_db():
        """Читает данные из файла базы данных и возвращает их."""
        try:
            with open(PATH_DB, 'r') as db_book:
                return json.load(db_book)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error reading the database, returning empty list.")
            return []  # Возвращаем пустой список в случае ошибки

    @staticmethod
    def write_db(load_data: dict):
        """Записывает данные в файл базы данных."""
        try:
            with open(PATH_DB, 'w', encoding='utf-8') as db_book:
                json.dump(load_data, db_book, indent=4)
        except Exception as e:
            print("Error writing to the database:", e)

    def get_unique_id(self) -> int:
        """Генерирует уникальное значение ID для создания книги."""
        if not self.data:
            return 1  # Начинаем с id = 1, если данных нет
        else:
            existing_id = {entry['id'] for entry in self.data}  # Сохраняем существующие id в множестве
            new_id = max(existing_id) + 1  # Увеличиваем максимальный id на 1
            return new_id

    def __iter__(self):
        """Возвращает итератор для обхода книг в базе данных."""
        self.index = 0  # Сбрасываем индекс для новой итерации
        return self

    def __next__(self):
        """Возвращает следующую книгу из базы данных."""
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration