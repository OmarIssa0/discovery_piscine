#! /usr/bin/env python3
num_first = input("Enter the first number:\n")
num_second = input("Enter the second number:\n")
num_result = int(num_first) * int(num_second)
print(f"{num_first} x {num_second} = {num_result}")
if num_result < 0:
    print("The result is negative.")
elif num_result == 0:
    print("This number is both positive and negative.")
else:
    print("The result is positive.")