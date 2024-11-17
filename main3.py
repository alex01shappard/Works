from pathlib import Path

# Функция для замены 'N/A' средним значением соседних чисел
def replace_na_with_average(row):
    numbers = row.split()
    # Преобразуем числа, заменяя 'N/A' на None
    values = [float(num) if num != 'N/A' else None for num in numbers]

    for i in range(len(values)):
        if values[i] is None:
            left = values[i - 1] if i > 0 else None
            right = values[i + 1] if i < len(values) - 1 else None
            # Берем среднее из соседних чисел, если они есть
            neighbors = [x for x in (left, right) if x is not None]
            values[i] = sum(neighbors) / len(neighbors) if neighbors else 0

    return values

# Функция для фильтрации: оставляем только отрицательные нечетные значения
def filter_row(values):
    return [x for x in values if x < 0 and int(x) % 2 != 0]

# Основная часть
def main():
    # Указываем пути к файлам
    input_file = Path('data/third_task.txt')
    output_file = Path('output3/output_task3.txt')

    # Считываем строки из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        rows = file.readlines()

    # Переменная для хранения результатов
    results = []

    for row in rows:
        # Заменяем 'N/A' средними значениями
        processed_row = replace_na_with_average(row)
        # Применяем фильтрацию
        filtered_row = filter_row(processed_row)
        # Рассчитываем среднее значение для строки
        average = sum(filtered_row) / len(filtered_row) if filtered_row else 0
        # Сохраняем результат
        results.append(average)

    # Записываем результаты в файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for avg in results:
            file.write(f'{avg:.2f}\n')

if __name__ == '__main__':
    main()
