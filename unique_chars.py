def count_unique_chars(s):
    unique_chars = set()  # множество для хранения уникальных символов
    for char in s:
        unique_chars.add(char)  # set автоматически исключает дубликаты
    return len(unique_chars)

# Пример использования
print(count_unique_chars("hello"))  # Выведет: 4
