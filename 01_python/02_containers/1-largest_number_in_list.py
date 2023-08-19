#!/usr/bin/env python3
"""Find the largest value in a given input"""

if __name__ == "__main__":
    data = input('Please enter a list of numbers separated by a comma:\n')
    try:
        data = [int(item)
                for item in data.split(",") if item.strip().isdecimal()]
    except ValueError:
        print("Invalid input")
        exit(1)

    if len(data) == 0:
        print("Empty List!!")
        exit(1)

    print(f"The largest value is {max(data)}")
