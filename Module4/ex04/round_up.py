#! /usr/bin/env python3

input_float = input("Give me a number: ")
number = float(input_float)
if number % 1 == 0:
    print(int(number))
else:
    print(int(number) + 1)