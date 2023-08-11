#!/usr/bin/env python3
# Prints a calendar month of a year
import calendar


def get_input(msg, validate):
    """Get input from user and validate it.

    Args:
        msg (str): The message to display.
        validate (function): The function to validate the input.

    Returns: int or None"""
    user_input = input(msg)
    if not user_input:
        exit(0)

    try:
        value = int(user_input)
    except Exception:
        return None

    if not validate(value):
        return None

    return value


if __name__ == "__main__":
    month = get_input("Enter a month: ", lambda x: x > 0 and x <= 12)
    if not month:
        print("Invalid month value")
        exit(1)

    year = get_input("Enter a year: ", lambda x: x > 0)
    if not year:
        print("Invalid year value")
        exit(1)

    print()
    print(calendar.month(year, month))
