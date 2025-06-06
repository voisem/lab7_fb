import csv  # Импортируем модуль csv для работы с CSV-файлами

# Открываем файл Books.csv в режиме записи ('w') с указанием newline=''
# newline='' нужен, чтобы не было пустых строк между записями
with open("Books.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # Создаем объект writer для записи строк в CSV

    # Записываем заголовок таблицы
    writer.writerow(["Наименование книги", "Писатель / Автор", "Страна автора", "Год издания"])

    # Записываем каждую строку данных по книге
    writer.writerow(["Властелин колец", "Джон Р. Р. Толкин", "Великобритания", 1954])
    writer.writerow(["Гордость и предубеждение", "Джейн Остин", "Великобритания", 1813])
    writer.writerow(["Тёмные начала", "Филип Пулман", "Великобритания", 1995])
    writer.writerow(["Автостопом по галактике", "Дуглас Адамс", "Великобритания", 1979])
    writer.writerow(["Гарри Поттер и Кубок огня", "Джоан Роулинг", "Великобритания", 2000])
    writer.writerow(["Убить пересмешника", "Харпер Ли", "США", 1960])
    writer.writerow(["Винни Пух", "Алан Александр Милн", "Великобритания", 1926])
    writer.writerow(["1984", "Джордж Оруэлл", "Великобритания", 1948])
    writer.writerow(["Лев, колдунья и платяной шкаф", "Клайв Стэйплз Льюис", "Великобритания", 1950])
    writer.writerow(["Джейн Эйр", "Шарлотта Бронте", "Великобритания", 1847])
    writer.writerow(["Уловка-22", "Джозеф Хеллер", "США", 1961])
    writer.writerow(["Грозовой перевал", "Эмили Бронте", "Великобритания", 1847])
    writer.writerow(["Пение птиц", "Себастьян Фолкс", "Великобритания", 1993])
    writer.writerow(["Ребекка", "Дафна Дюморье", "Великобритания", 1938])
    writer.writerow(["Над пропастью во ржи", "Джером Сэлинджер", "США", 1951])
    writer.writerow(["Ветер в ивах", "Кеннет Грэм", "Великобритания", 1908])
    writer.writerow(["Большие надежды", "Чарльз Диккенс", "Великобритания", 1861])
    writer.writerow(["Маленькие женщины", "Луиза Мэй Олкотт", "США", 1868])
    writer.writerow(["Война и мир", "Лев Толстой", "Россия", 1865])
    writer.writerow(["Унесённые ветром", "Маргарет Митчелл", "США", 1936])
    writer.writerow(["Гарри Поттер и философский камень", "Джоан Роулинг", "Великобритания", 1997])
