#! /usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")
else:
    index = len(sys.argv) - 1
    while index > 0:
        print(sys.argv[index])
        index -= 1