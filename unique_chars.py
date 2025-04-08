def count_unique_chars(s):
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
    return len(unique_chars)


print(count_unique_chars("hello"))
