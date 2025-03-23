#! /usr/bin/env python3

column = 0
row = 0 
while row <= 10:
    if row != 0:
        print()
    print("Table of", row ,end=": ")
    while column <= 10:
        rust = row * column
        print(rust, end=" ")
        column += 1
    row += 1
    column = 0