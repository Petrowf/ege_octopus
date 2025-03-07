abc = '0123456789abcdef'
for x in abc:
    n = int(f"2{x}84", 19) + int(f"2b3{x}", 16)
    if n % 88 == 0:
        print(x, n//88)