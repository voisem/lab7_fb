import csv  # Импортируем модуль для работы с CSV-файлами

# Создаём класс для работы с книгами в CSV
class BooksCSV:
    def __init__(self, filename):
        self.filename = filename  # Сохраняем имя файла как свойство объекта
    def read_rows(self):
        with open(self.filename, 'r', encoding='utf-8') as file:  # Открываем файл для чтения
            return list(csv.reader(file))  # Читаем все строки и возвращаем как список
    def write_rows(self, rows):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:  # Открываем файл для записи
            csv.writer(file).writerows(rows)  # Записываем все строки в файл
    def search_by_author(self, author):
        rows = self.read_rows()  # Получаем все строки из файла
        found = False  # Переменная для отслеживания, найден ли автор
        for row in rows[1:]:  # Пропускаем заголовок и перебираем строки
            if author.lower() in row[1].lower():  # Сравниваем имя автора (без учёта регистра)
                print(row)  # Печатаем строку, если автор найден
                found = True  # Отмечаем, что нашли хотя бы одну книгу
        if not found:  # Если ничего не найдено
            print("Книги не найдены.")  # Выводим сообщение об отсутствии результата
    def search_by_year_range(self, start, end):
        rows = self.read_rows()  # Получаем все строки из файла
        for row in rows[1:]:  # Пропускаем заголовок и перебираем строки
            year = int(row[3])  # Преобразуем строку с годом в число
            if start <= year <= end:  # Проверяем, входит ли год в диапазон
                print(row)  # Печатаем подходящую строку
    def show_with_numbers(self):
        for i, row in enumerate(self.read_rows(), start=1):  # Перебираем строки с нумерацией
            print(f"{i}: {row}")  # Выводим строку с её номером
    def edit_or_delete(self):
        rows = self.read_rows()  # Читаем все строки
        for i, row in enumerate(rows):  # Показываем все строки с номерами
            print(f"{i}: {row}")

        index = int(input("Введите номер строки: "))  # Получаем индекс строки от пользователя
        if not (0 <= index < len(rows)):  # Проверяем корректность номера
            print("Неверный номер.")  # Сообщаем об ошибке
            return  # Выходим из функции

        action = input("1 — удалить, 2 — изменить: ")  # Запрашиваем действие у пользователя

        if action == "1":  # Если выбрано удаление
            del rows[index]  # Удаляем строку из списка
            print("Удалено.")  # Подтверждаем удаление

        elif action == "2":  # Если выбрано редактирование
            title = input("Новое название: ")  # Вводим новое название
            author = input("Новый автор: ")  # Вводим нового автора
            country = input("Новая страна: ")  # Вводим страну автора
            year = input("Новый год: ")  # Вводим новый год
            rows[index] = [title, author, country, year]  # Обновляем строку новыми данными
            print("Изменено.")  # Подтверждаем изменение

        else:  # Если введена неправильная команда
            print("Неверная команда.")  # Сообщаем об ошибке
            return  # Выходим из функции

        self.write_rows(rows)  # Сохраняем обновлённый список строк в файл
    def menu(self):
        while True:  # Запускаем бесконечный цикл меню
            print("\n1. Найти книги по автору")  # Пункт 1
            print("2. Найти книги по диапазону лет")  # Пункт 2
            print("3. Показать все с номерами")  # Пункт 3
            print("4. Удалить или изменить строку")  # Пункт 4
            print("5. Выход")  # Пункт 5

            choice = input("Выберите действие: ")  # Получаем выбор пользователя

            if choice == "1":  # Если выбран пункт 1
                self.search_by_author(input("Автор: "))  # Запрашиваем автора и ищем
            elif choice == "2":  # Если выбран пункт 2
                start = int(input("Начальный год: "))  # Запрашиваем начальный год
                end = int(input("Конечный год: "))  # Запрашиваем конечный год
                self.search_by_year_range(start, end)  # Вызываем поиск по диапазону
            elif choice == "3":  # Если выбран пункт 3
                self.show_with_numbers()  # Показываем все строки с номерами
            elif choice == "4":  # Если выбран пункт 4
                self.edit_or_delete()  # Запускаем редактирование или удаление
            elif choice == "5":  # Если выбран выход
                print("Выход.")  # Печатаем сообщение
                break  # Прерываем цикл
            else:  # Если введено некорректное значение
                print("Ошибка ввода.")  # Сообщаем об ошибке


# Создаём объект класса с файлом Books.csv
books = BooksCSV("Books.csv")  # Указываем имя CSV-файла
books.search_by_author("Роулинг")  # Выведет все книги автора "Роулинг"
books.search_by_year_range(1900, 2000)  # Найдёт все книги, изданные между 1900 и 2000 годами включительно
books.show_with_numbers()  # Выведет все книги с номерами строк
books.edit_or_delete()  # Запустит интерактивный режим: ты выберешь строку и действие (удалить или изменить)
books.menu()  # Запустит меню: можно выбирать действия по номерам (поиск, вывод, редактирование и т.д.)


