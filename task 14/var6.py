for x in '0123456789abcdefghijklm':
    a = int(f"2{x}{x}341011", 23)
    b = int(f"220{x}4", 23)
    c = int(f"110{x}6", 23)
    n = a + b + c
    if n % 22 == 0:
        print(x,n / 22)