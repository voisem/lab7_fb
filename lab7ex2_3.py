import csv


# Запрашиваем количество записей для добавления
n = int(input("Сколько новых книг вы хотите добавить?: "))

# Открываем файл для добавления новых строк
with open("Books.csv", "a", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for i in range(n):
        print(f"Запись {i + 1}")
        title = input("Название книги: ")
        author = input("Автор: ")
        country = input("Страна автора: ")
        year = input("Год издания: ")
        writer.writerow([title, author, country, year])  # Добавляем запись
