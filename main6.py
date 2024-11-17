import requests
import os
import json

def fetch_data_from_api():
    # URL публичного API JSONPlaceholder
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # Запрос данных
    response = requests.get(api_url)

    # Проверяем статус ответа
    if response.status_code == 200:
        return response.json()  # Возвращаем JSON-данные
    else:
        raise Exception(f"Ошибка: API вернул статус {response.status_code}")

def save_json_to_file(data, filename):
    # Сохраняем JSON в файл
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def generate_html(json_data):
    # Начало HTML-документа
    html = "<!DOCTYPE html>\n<html>\n<head>\n<title>API Data</title>\n</head>\n<body>\n"
    html += "<h1>Данные из API</h1>\n<ul>\n"

    # Преобразуем каждый элемент JSON в HTML
    for item in json_data:
        html += f"<li><strong>Post ID:</strong> {item['id']}<br>"
        html += f"<strong>Title:</strong> {item['title']}<br>"
        html += f"<strong>Body:</strong> {item['body']}</li><hr>\n"

    # Завершение HTML-документа
    html += "</ul>\n</body>\n</html>"
    return html

def save_html_to_file(html, filename):
    # Сохраняем HTML в файл
    with open(filename, "w", encoding="utf-8") as html_file:
        html_file.write(html)

def main():
    # Создаем директорию output6, если она недоступна
    output_dir = 'output6'
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Получение данных из API
        json_data = fetch_data_from_api()

        # Сохранение JSON в файл
        json_filename = os.path.join(output_dir, 'api_data.json')
        save_json_to_file(json_data, json_filename)
        print(f"JSON файл успешно создан: {json_filename}")

        # Генерация HTML
        html_content = generate_html(json_data)

        # Сохранение HTML в файл
        html_filename = os.path.join(output_dir, 'api_data.html')
        save_html_to_file(html_content, html_filename)
        print(f"HTML файл успешно создан: {html_filename}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
