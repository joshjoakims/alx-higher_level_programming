#!/usr/bin/python3
from add_0 import add  # Import the add function first

def print_addition(a, b):
    print(f"{a} + {b} = {add(a, b)}")

if __name__ == "__main__":
    a = 1
    b = 2
    print_addition(a, b)

