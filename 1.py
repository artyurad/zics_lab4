#!/usr/bin/python3


import csv


def calculate_letter_frequencies(file_path):
    # Створюємо словник для зберігання частот літер
    letter_frequencies = {letter: 0 for letter in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Зчитуємо вміст файлу та перетворюємо його на рядок
            content = file.read().lower()

            # Видаляємо всі символи пунктуації, залишаючи лише пробіли
            content = ''.join(char if char == ' ' or char.isalpha() else '' for char in content)

            # Обчислюємо частоти літер
            for char in content:
                if char in letter_frequencies:
                    letter_frequencies[char] += 1
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу '{file_path}': {e}")
        return None

    return letter_frequencies

def save_to_csv(file_path, letter_frequencies):
    try:
        with open(file_path + '_frequencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Letter', 'Frequency'])

            # Сортуємо літери за алфавітом
            sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[0])

            for letter, frequency in sorted_frequencies:
                csvwriter.writerow([letter, frequency])

        print(f"Частоти для файлу '{file_path}' збережено в '{file_path}_frequencies.csv'")
    except Exception as e:
        print(f"Помилка при збереженні частот для файлу '{file_path}': {e}")

def main():
    # Приклад виклику функції зі списком файлів
    file_paths = ['1.txt', '2.txt', "3.txt"]

    for file_path in file_paths:
        frequencies = calculate_letter_frequencies(file_path)

        if frequencies:
            # Виводимо літери по частоті у консоль
            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
            print(f"Літери для файлу '{file_path}' по мірі спадання частоти:")
            for letter, _ in sorted_frequencies:
                print(letter, end=' ')
            print()  # Перехід на новий рядок

            # Зберігаємо частоти у CSV-файл
            save_to_csv(file_path, frequencies)

if __name__ == "__main__":
    main()
