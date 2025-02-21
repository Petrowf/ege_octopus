print('w x y z 1 2')
for w in [0, 1]:
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                f1 = (x == y) or (w <= z)
                f2 = (x <= y) <= (w == z)
                if w == 1 and x == 0 and f1 == 1:
                    print(w, x, y, z, f1, f2)