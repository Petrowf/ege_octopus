print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = x and (z <= w) and not(y)
                if f == 1:
                    print(w, x, y, z, f)