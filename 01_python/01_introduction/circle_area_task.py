#!/usr/bin/env python3
# Calculate the area of a circle
import math

while 1:
    user_input = input("Enter the radius of the circle: ")
    if not user_input:
        break

    try:
        radius = float(user_input)
    except Exception:
        print("Invalid input")
        continue

    if radius < 0:
        print("Radius cannot be negative")
        continue

    area = round(math.pi * radius ** 2, 2)
    print(
        f"The area of the circle with radius {radius} is {area} units squared")
    print()
