#! /usr/bin/env python3

list = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", list)
list2 = []
i = 0
while i < len(list):
    list2.append(list[i] + 2)
    i += 1
print("New array:", list2)