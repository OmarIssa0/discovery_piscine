#! /usr/bin/env python3

import sys
if len(sys.argv) > 1:
    string = sys.argv[1]
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")
else:
    print("Number of parameters: 0.")