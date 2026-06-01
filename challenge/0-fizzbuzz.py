#!/usr/bin/env python3
"""
Fix My Code Challenge - FizzBuzz
Prints numbers from 1 to N with FizzBuzz substitutions.
"""

import sys

def fizzbuzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        fizzbuzz(n)
        print("")  # newline at the end
    except ValueError:
        print("N must be an integer")
        sys.exit(1)
