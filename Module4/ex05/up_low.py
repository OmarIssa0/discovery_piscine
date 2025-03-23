#! /usr/bin/env python3
input_string = input("")
int = 0
while int < len(input_string):
    if input_string[int].isupper():
        print(input_string[int].lower(), end="")
    else:
        print(input_string[int].upper(), end="")
    int += 1