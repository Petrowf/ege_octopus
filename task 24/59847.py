"""Текстовый файл состоит из символов T, U, V, W, X, Y и Z. Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности), среди которых пара символов W встречается ровно 100 раз."""
with open("59847.txt", encoding="utf-8") as file:
    text = file.read()

text = text.replace("WW", "!")
split_text = text.split("!")
max_len = 0
for i in range(len(split_text)-101):
    posl = ''.join(split_text[i:i+101])
    max_len = max(max_len, len(posl) + 100*2)

print(max_len)

