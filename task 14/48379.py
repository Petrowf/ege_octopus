abc = '012345678'
for a in range(1, 1000):
    for x in abc:
        m = int(f"842{x}5", 9)
        n = int(f"8{x}725", 9)
        if (m + a) % n == 0:
            print(a)