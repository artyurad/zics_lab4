#!/usr/bin/python3


import csv
from collections import Counter


def is_ukrainian(char):
    ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return char in ukr_alphabet

def calculate_bigram_frequencies(file_paths):
    all_bigrams = Counter()

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower().replace('\n', ' ')

                # Видаляємо всі символи пунктуації та пробіли
                content = ''.join(char if is_ukrainian(char) else ' ' for char in content)

                bigrams = [content[i:i+2] for i in range(len(content)-1) if ' ' not in content[i:i+2]]
                all_bigrams.update(bigrams)
        except FileNotFoundError:
            print(f"Файл '{file_path}' не знайдено.")
        except Exception as e:
            print(f"Помилка при обробці файлу '{file_path}': {e}")

    return all_bigrams

def save_bigram_to_csv(file_path, bigram_frequencies):
    try:
        with open(file_path + '_bigram_frequencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Bigram', 'Frequency', 'Relative Frequency'])

            total_bigrams = sum(bigram_frequencies.values())

            # Сортуємо біграми за відносною частотою у зменшуючому порядку
            sorted_bigrams = sorted(bigram_frequencies.items(), key=lambda x: x[1], reverse=True)

            for bigram, frequency in sorted_bigrams:
                relative_frequency = frequency / total_bigrams
                csvwriter.writerow([bigram, frequency, relative_frequency])

        print(f"Біграми для файлу '{file_path}' збережено в '{file_path}_bigram_frequencies.csv'")
    except Exception as e:
        print(f"Помилка при збереженні біграм для файлу '{file_path}': {e}")

def main():
    file_paths = ['1.txt', '2.txt']

    for file_path in file_paths:
        bigram_frequencies = calculate_bigram_frequencies([file_path])

        if bigram_frequencies:
            # Збереження біграм у CSV-файл
            save_bigram_to_csv(file_path, bigram_frequencies)

            # Виведення 30 найбільш імовірних біграм у консоль
            top_30_bigrams = [bigram for bigram, _ in bigram_frequencies.most_common(30)]
            print(f"30 найбільш імовірних біграм для файлу '{file_path}':")
            print(', '.join(top_30_bigrams))
            print()

if __name__ == "__main__":
    main()
