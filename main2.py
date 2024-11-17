from pathlib import Path

# Функция для обработки строки: суммирование абсолютных значений чисел, квадрат которых меньше 100000
def process_row(row):
    # Преобразуем строку в список чисел
    numbers = map(float, row.split())
    # Фильтруем числа, квадрат которых меньше 100000, и считаем их абсолютные значения
    filtered_numbers = [abs(num) for num in numbers if num ** 2 < 100000]
    # Возвращаем сумму абсолютных значений
    return sum(filtered_numbers)

# Основная часть
def main():
    # Указываем путь к входному файлу и выходному файлу
    input_file = Path('data/second_task.txt')
    output_file = Path('output2/output_task2.txt')

    # Считываем строки из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        rows = file.readlines()

    # Применяем обработку к каждой строке
    column = [process_row(row) for row in rows]

    # Считаем среднее арифметическое значения для столбца
    average = sum(column) / len(column) if column else 0

    # Записываем результаты в файл
    with open(output_file, 'w', encoding='utf-8') as file:
        # Записываем каждое значение столбца в отдельную строку
        for value in column:
            file.write(f'{value:.2f}\n')
        # Записываем среднее арифметическое в конце
        file.write(f'Average: {average:.2f}\n')


if __name__ == '__main__':
    main()
