"""Класс для навигации по меню операций с базой данных книг"""
from src.operations_database import OperationsDataBase


class MenuNavigator(OperationsDataBase):
    #Выполняет действие в зависимости выбора пользователя в меню.
    # Возвращает True если пользователь выполнил действие или None
    # если пользователь выбрал выход из меню
    def actions(self) -> bool | None:
        menu = self.get_safe_action()
        if menu is None:  # Проверяем, вернул ли метод None когда ввел "exit"
            return None
        if menu == '1':
            self.create_book()
        elif menu == '2':
            self.del_book()
        elif menu == '3':
            self.search_book()
        elif menu == '4':
            self.show_all_books()
        elif menu == '5':
            self.update_status()
        return  True

    def permanent_action(self) -> None:
        # выполняет действие пока пользователь не решит выйти
        while True:
            result = self.actions()
            if result is None:
                break