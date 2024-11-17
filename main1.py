import re
from collections import Counter
from pathlib import Path

# Функция для подсчета частоты слов
def count_word_frequency(text):
    # Приводим текст к нижнему регистру и удаляем ненужные символы
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Функция для подсчета среднего количества предложений в абзацах
def average_sentences_per_paragraph(text):
    paragraphs = [p for p in text.split('\n') if p.strip()]  # Разделяем на абзацы, исключая пустые строки
    sentence_counts = [
        len(re.findall(r'[.!?]', paragraph)) for paragraph in paragraphs
    ]
    return sum(sentence_counts) / len(paragraphs) if paragraphs else 0

# Основная часть
def main():
    # Указываем путь к входящему файлу
    input_file = Path('data/first_task.txt')
    # Указываем пути к выходящим файлам
    output_common_file = Path('output1/word_frequency.txt')
    output_variant_file = Path('output1/average_sentences.txt')

    # Считываем текст из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Общая часть: подсчет частоты слов
    word_freq = count_word_frequency(text)
    # Сортируем по убыванию частоты
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Записываем результаты общей части в файл
    with open(output_common_file, 'w', encoding='utf-8') as file:
        for word, freq in sorted_word_freq:
            file.write(f'{word}:{freq}\n')

    # Вариантная часть: среднее количество предложений в абзацах
    avg_sentences = average_sentences_per_paragraph(text)

    # Записываем результат вариантной части в файл
    with open(output_variant_file, 'w', encoding='utf-8') as file:
        file.write(f'{avg_sentences:.2f}\n')


if __name__ == '__main__':
    main()
