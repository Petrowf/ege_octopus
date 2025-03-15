s = "1"*2024

while '11111'in s or '222' in s:
    if '11111' in s:
        s = s.replace('11111', '22', 1)