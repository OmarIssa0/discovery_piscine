#! /usr/bin/env python3
num = input("Enter a number\n")
num = int(num)
i = 0
while i < 10:
    print(f"{i} x {num} = {num * i}")
    i += 1