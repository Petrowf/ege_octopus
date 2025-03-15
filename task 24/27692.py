with open("27692.txt", encoding="utf-8") as file:
    text = file.read()
cnt_cur = 0
cnt_max = 0

for char in text:
    if char == "B":
        cnt_cur += 1
        cnt_max = max(cnt_cur, cnt_max)
    else:
        cnt_cur = 0

print(cnt_max)
