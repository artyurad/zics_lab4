#!/usr/bin/python3


import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def is_ukrainian(char):
    ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return char in ukr_alphabet

def calculate_bigram_frequencies(file_path):
    bigram_frequencies = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower().replace('\n', ' ')
            content = ''.join(char if is_ukrainian(char) else ' ' for char in content)

            bigrams = [content[i:i+2] for i in range(len(content)-1) if ' ' not in content[i:i+2]]
            bigram_frequencies.update(bigrams)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу '{file_path}': {e}")

    return bigram_frequencies

def plot_bigram_matrix(bigram_matrix, file_path):
    ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    matrix_size = len(ukr_alphabet)
    matrix = np.zeros((matrix_size, matrix_size))

    for i, char1 in enumerate(ukr_alphabet):
        for j, char2 in enumerate(ukr_alphabet):
            bigram = char1 + char2
            matrix[i, j] = bigram_matrix[bigram]

    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.xticks(np.arange(matrix_size), list(ukr_alphabet))
    plt.yticks(np.arange(matrix_size), list(ukr_alphabet))
    plt.xlabel('Другий символ біграми')
    plt.ylabel('Перший символ біграми')
    plt.title(f'Матриця частот біграм для файлу {file_path}')
    plt.colorbar(label='Частота')
    plt.show()

def main():
    file_paths = ['1.txt', '2.txt']

    for file_path in file_paths:
        # Збираємо біграми та їх частоти
        bigram_frequencies = calculate_bigram_frequencies(file_path)

        if bigram_frequencies:
            # Створюємо та візуалізуємо матрицю біграм
            plot_bigram_matrix(bigram_frequencies, file_path)

if __name__ == "__main__":
    main()
