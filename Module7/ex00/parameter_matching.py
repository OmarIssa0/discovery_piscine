#! /usr/bin/env python3

import sys
if len(sys.argv) < 2:
    print("none")
    sys.exit(1)
input_string = input("What was the parameter? ") 
if input_string == sys.argv[1]:
    print("Good job!")
else:
    print("Nope, sorry...")