import collections
import re

def analyze_text(text):
    text_lower = text.lower()
    cleaned_text = re.sub(r'[^a-zа-я\s]', '', text_lower)
    words = cleaned_text.split()
    words = [word for word in words if word]
    characters = [char for char in text_lower if 'a' <= char <= 'z' or 'а' <= char <= 'я']

    print(f"\n--- Исходный текст (частично): {text[:100]}... ---")
    print(f"Количество слов: {len(words)}")
    print(f"Количество букв: {len(characters)}")

    word_counts = collections.Counter(words)
    char_counts = collections.Counter(characters)

    print("\n--- 5 самых популярных слов ---")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count} раз(а)")

    print("\n--- 5 самых популярных букв ---")
    for char, count in char_counts.most_common(5):
        print(f"'{char}': {count} раз(а)")

if __name__ == "__main__":
    print("Добро пожаловать в анализатор текста!")
    print("Пожалуйста, введите длинную строку текста (или вставьте готовый текст).")
    print("Для завершения ввода нажмите Enter дважды.")

    input_lines = []
    while True:
        line = input()
        if not line: 
            break
        input_lines.append(line)

    long_text = " ".join(input_lines)

    if not long_text.strip():
        print("Вы не ввели текст. Анализ невозможен.")
    else:
        analyze_text(long_text)

    print("\nАнализ завершен.")


if __name__ == "__main__":
    pass # Ваш код здесь
