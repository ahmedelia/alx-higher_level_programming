#!/usr/bin/python3
num = 0
for i in range(122, 96, -1):
    if (i % 2 == 0):
        num = 0
    else:
        num = 32
    print(chr(i - num), end="")
