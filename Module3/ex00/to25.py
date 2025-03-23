#! /usr/bin/env python3
num = input("Enter a number less then 25\n")
if num > "25":
    print("Error")
else:
    num = int(num)
    while num <= 25:
        print("Inside the loop, my variable is " + str(num))
        num += 1
