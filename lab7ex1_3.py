


# Открываем файл в режиме чтения
with open("Students.txt", "r") as file:
    names = file.readlines()  # Читаем все строки в список

# Выводим все имена на экран
print("Все имена в файле:")
for name in names:
    print(name.strip())  # Убираем символ новой строки при выводе

# Запрашиваем имя для поиска
search_name = input("Введите имя, которое хотите найти в файле: ")

# Проверяем, есть ли имя в списке имён
if any(search_name + "\n" == name for name in names):
    print(f"Имя '{search_name}' найдено в файле.")

    # Сохраняем найденное имя в отдельный файл
    with open("FoundName.txt", "w") as found_file:
        found_file.write(search_name + "\n")  # Записываем имя в файл

    # Создаем файл без найденного имени
    with open("RemainingNames.txt", "w") as remaining_file:
        for name in names:
            if name.strip() != search_name:
                remaining_file.write(name)  # Записываем только имена, не равные искомому
else:
    print(f"Имя '{search_name}' не найдено в файле.")
