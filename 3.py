#!/usr/bin/python3


import csv
from collections import Counter

def is_ukrainian(char):
    ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return char in ukr_alphabet

def calculate_trigram_frequencies(file_paths):
    all_trigrams = Counter()

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower().replace('\n', ' ')

                # Видаляємо всі символи пунктуації та пробіли
                content = ''.join(char if is_ukrainian(char) else ' ' for char in content)

                trigrams = [content[i:i+3] for i in range(len(content)-2) if ' ' not in content[i:i+3]]
                all_trigrams.update(trigrams)
        except FileNotFoundError:
            print(f"Файл '{file_path}' не знайдено.")
        except Exception as e:
            print(f"Помилка при обробці файлу '{file_path}': {e}")

    return all_trigrams

def save_trigram_to_csv(file_path, trigram_frequencies):
    try:
        with open(file_path + '_trigram_frequencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Trigram', 'Frequency', 'Relative Frequency'])

            total_trigrams = sum(trigram_frequencies.values())

            # Сортуємо триграми за відносною частотою у зменшуючому порядку
            sorted_trigrams = sorted(trigram_frequencies.items(), key=lambda x: x[1], reverse=True)

            for trigram, frequency in sorted_trigrams:
                relative_frequency = frequency / total_trigrams
                csvwriter.writerow([trigram, frequency, relative_frequency])

        print(f"Триграми для файлу '{file_path}' збережено в '{file_path}_trigram_frequencies.csv'")
    except Exception as e:
        print(f"Помилка при збереженні триграм для файлу '{file_path}': {e}")

def main():
    file_paths = ['1.txt', '2.txt', '3.txt']

    for file_path in file_paths:
        trigram_frequencies = calculate_trigram_frequencies([file_path])

        if trigram_frequencies:
            # Збереження триграм у CSV-файл
            save_trigram_to_csv(file_path, trigram_frequencies)

            # Виведення 30 найбільш імовірних триграм у консоль
            top_30_trigrams = [trigram for trigram, _ in trigram_frequencies.most_common(30)]
            print(f"30 найбільш імовірних триграм для файлу '{file_path}':")
            print(', '.join(top_30_trigrams))
            print()

if __name__ == "__main__":
    main()
