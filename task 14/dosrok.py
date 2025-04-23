for x in ('0123456789ABCDEFGHIJK'):
    n = int(f"82934{x}2", 21) + int(f"2924{x}{x}7", 21) + int(f"67564{x}8", 21)
    if n % 20 == 0:
        print(x, n // 20)