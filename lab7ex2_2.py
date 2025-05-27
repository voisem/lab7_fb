import csv

# Запрашиваем у пользователя данные новой книги
title = input("Введите название книги: ")
author = input("Введите имя автора: ")
country = input("Введите страну автора: ")
year = input("Введите год издания: ")

# Открываем CSV-файл в режиме добавления ('a')
with open("Books.csv", "a", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([title, author, country, year])  # Записываем введённые данные

# Открываем CSV-файл в режиме чтения, чтобы вывести все строки
with open("Books.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Выводим каждую строку файла
