"""Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых каждая из букв C и D встречается не более двух раз."""
with open("63073.txt", encoding="utf-8") as file:
    text = file.read()

split_text = text.replace("C", "C ").replace("D", "D ").split()
max_len = 0
for i in range(len(split_text)-5):
    s = ''.join(split_text[i:i+5])[:-1]
    if s.count("C") == 2 and s.count("D") == 2:
        max_len = max(max_len, len(s))
    # elif s.count("C") == 1 or s.count("D") == 1:
    #     max_len = max(max_len, len(s))
    # else:
    #     max_len = max(max_len, len(s))
print(max_len)