#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        if i != j:
            print("{}{}".format(i, j), end=', ')
print("89", end='\n')
