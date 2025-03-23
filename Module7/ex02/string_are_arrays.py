#! /usr/bin/env python3

import sys

if len(sys.argv) == 2:
    i = len(sys.argv[1]) - 1
    count = 0
    while i >= 0:
        if sys.argv[1][i] == "z":
            count += 1
            print("z" , end="")
        i -= 1
    if count == 0:
        print("none")
else:
    print("none")