# Используем библиотеку beautifulsoup

from bs4 import BeautifulSoup
import csv
from pathlib import Path

# Чтение HTML-файла
input_file = Path("data/fifth_task.html")
html_content = input_file.read_text(encoding="utf-8")

# Парсинг HTML с использованием BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Поиск таблицы в HTML
table = soup.find("table")  # Если таблиц несколько, уточните поиск, например, добавив атрибут class

# Извлечение данных из таблицы
rows = []
for row in table.find_all("tr"):  # Проходим по строкам таблицы
    cells = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]  # Считываем текст ячеек
    rows.append(cells)

# Запись данных в CSV-файл
output_file = Path("output5/output.csv")
with output_file.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Данные таблицы успешно сохранены в файл {output_file}.")
