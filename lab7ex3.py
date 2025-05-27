import requests  # Импортируем библиотеку для HTTP-запросов
import sys       # Для выхода из программы при ошибках
from typing import Tuple, Dict, Any  # Типизация для читаемости кода
from datetime import datetime, timezone, timedelta  # Для работы с датой и временем


API_KEY = "13ff878c18f67d9be7da4fd7ffc3b90f"  # Ключ API OpenWeatherMap


def get_location() -> Tuple[str, float, float]:
    """Автоопределение местоположения по IP"""
    try:
        resp = requests.get("https://ipinfo.io/json", timeout=5)  # Запрашиваем данные о местоположении
        resp.raise_for_status()  # Проверяем статус ответа
        data = resp.json()  # Парсим JSON
        city = data.get("city", "Неизвестно")  # Берём город или "Неизвестно"
        loc = data.get("loc")  # Получаем координаты
        if not loc:  # Если координат нет
            raise ValueError("Координаты не найдены")  # Ошибка
        lat, lon = map(float, loc.split(","))  # Разбиваем строку координат на float
        return city, lat, lon  # Возвращаем город, широту и долготу
    except Exception as e:  # Обработка любых ошибок
        print(f"[Ошибка] Не удалось определить локацию: {e}")  # Вывод ошибки
        sys.exit(1)  # Завершаем программу


def get_weather(lat: float, lon: float) -> Dict[str, Any]:
    """Получение данных погоды по координатам"""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru"
    )  # Формируем URL для запроса с параметрами
    try:
        resp = requests.get(url, timeout=7)  # Делаем запрос с таймаутом
        resp.raise_for_status()  # Проверяем статус ответа
        return resp.json()  # Возвращаем JSON с погодой
    except requests.HTTPError:  # Если HTTP ошибка
        print(f"[Ошибка HTTP] Статус: {resp.status_code} - {resp.text}")  # Выводим статус и текст
        sys.exit(1)  # Завершаем программу
    except requests.RequestException as e:  # Другие ошибки запроса
        print(f"[Ошибка запроса] {e}")  # Выводим ошибку
        sys.exit(1)  # Завершаем программу


def format_time(unix_timestamp: int, tz_offset: int) -> str:
    """Преобразование UNIX-времени в строку с учётом часового пояса"""
    local_tz = timezone(timedelta(seconds=tz_offset))  # Создаём локальный timezone
    dt_local = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc).astimezone(local_tz)  # Конвертируем время
    return dt_local.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем в строку


def weather_ascii(icon: str) -> str:
    """Возвращает эмодзи и описание по коду иконки погоды"""
    icons = {
        "01d": "☀️  Ясно", "01n": "🌙  Ясно ночью",
        "02d": "⛅  Малооблачно", "02n": "☁️  Малооблачно ночью",
        "03d": "☁️  Облачно", "03n": "☁️  Облачно ночью",
        "04d": "☁️☁️  Пасмурно", "04n": "☁️☁️  Пасмурно ночью",
        "09d": "🌧️  Ливень", "09n": "🌧️  Ливень ночью",
        "10d": "🌦️  Дождь", "10n": "🌦️  Дождь ночью",
        "11d": "⛈️  Гроза", "11n": "⛈️  Гроза ночью",
        "13d": "❄️  Снег", "13n": "❄️  Снег ночью",
        "50d": "🌫️  Туман", "50n": "🌫️  Туман ночью",
    }  # Словарь иконок и описаний
    return icons.get(icon, "❓ Погода неизвестна")  # Возвращаем описание или "неизвестна"


def display_weather(data: Dict[str, Any], city: str) -> None:
    """Выводит на экран отформатированную погоду"""
    main = data.get("main", {})  # Получаем блок main
    weather = data.get("weather", [{}])[0]  # Получаем первый элемент weather
    wind = data.get("wind", {})  # Получаем данные о ветре
    sys_info = data.get("sys", {})  # Получаем системные данные (солнце)
    tz_offset = data.get("timezone", 0)  # Смещение часового пояса

    print("\n" + "="*40)  # Разделитель
    print(f"🌍 Погода в городе: {city}")  # Заголовок с городом
    print("="*40)  # Разделитель

    print(weather_ascii(weather.get("icon", "")))  # Выводим ASCII-иконку погоды
    print(f"Описание: {weather.get('description', '').capitalize()}")  # Описание погоды

    print(f"Температура: {main.get('temp')}°C (ощущается как {main.get('feels_like')}°C)")  # Темп. и ощущается
    print(f"Влажность: {main.get('humidity')}%")  # Влажность
    print(f"Давление: {main.get('pressure')} гПа")  # Давление

    print(f"Ветер: {wind.get('speed')} м/с, направление: {wind.get('deg', 0)}°")  # Скорость и направление ветра

    # Если есть время восхода и заката — выводим их с форматированием
    if (sunrise := sys_info.get("sunrise")) and (sunset := sys_info.get("sunset")):
        print(f"Восход солнца: {format_time(sunrise, tz_offset)}")
        print(f"Закат солнца: {format_time(sunset, tz_offset)}")

    print("="*40 + "\n")  # Конец блока с разделителем


def main():
    print("Определяем ваше местоположение по IP... 🌐")  # Лог начала определения
    city, lat, lon = get_location()  # Получаем город и координаты
    print(f"Ваш город: {city} (широта: {lat}, долгота: {lon})")  # Выводим данные о местоположении

    print("\nЗапрашиваем данные о погоде... ☁️")  # Лог запроса погоды
    weather_data = get_weather(lat, lon)  # Получаем погоду

    display_weather(weather_data, city)  # Выводим данные красиво


if __name__ == "__main__":
    main()  # Запускаем основной код
