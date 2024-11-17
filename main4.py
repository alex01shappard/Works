import pandas as pd
from pathlib import Path
import csv

# Перевод файла из формата txt в csv
txt_file = "data/fourth_task.txt"
csv_file = "data/fourth_task1.csv"

with open(txt_file, "r", encoding="utf-8") as infile, open(csv_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(row)

print(f"Файл успешно преобразован в {csv_file}")

def main():
    # Пути к входному и выходным файлам
    input_csv = Path('data/fourth_task1.csv')
    output_csv = Path('output4/modified_task4.csv')
    output_stats = Path('output4/statistics_task4.csv')

    # Считываем CSV-файл
    df = pd.read_csv(input_csv)

    # 1. Удаление столбца expiration_date
    if 'expiration_date' in df.columns:
        df = df.drop(columns=['expiration_date'])

    # 2. Среднее арифметическое по столбцу rating
    mean_rating = df['rating'].mean()

    # 3. Максимум по столбцу rating
    max_rating = df['rating'].max()

    # 4. Минимум по столбцу rating
    min_rating = df['rating'].min()

    # 5. Фильтрация по значению price < 9425
    filtered_df = df[df['price'] < 9425]

    # Запись статистики в текстовый файл
    with open(output_stats, 'w', encoding='utf-8') as stats_file:
        stats_file.write(f'Среднее значение рейтинга: {mean_rating:.2f}\n')
        stats_file.write(f'Максимальный рейтинг: {max_rating:.2f}\n')
        stats_file.write(f'Минимальный рейтинг: {min_rating:.2f}\n')

    # Запись модифицированной таблицы в CSV
    filtered_df.to_csv(output_csv, index=False)

if __name__ == '__main__':
    main()
