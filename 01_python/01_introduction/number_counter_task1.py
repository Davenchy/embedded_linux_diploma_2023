#!/usr/bin/env python3
# count the occurrence of a number in a list of numbers

# request user input
numbers_input = input("Enter a list of numbers separated by space:\n> ")


# remove extra whitespaces and split into a list
numbers = numbers_input.strip().split()

# filter the list and only get items with digits
numbers = filter(lambda x: x.isdigit(), numbers)

# convert filter object into a list of integers
numbers = list(map(lambda x: int(x), numbers))

while 1:
    number_to_count_input = input("\nEnter a number to count its occurrence \
[or nothing to quit]: ")

    if not number_to_count_input:
        break

    number_to_count = int(number_to_count_input)
    count = numbers.count(number_to_count)

    print(f"\nThe list: [{', '.join([str(c) for c in numbers])}]")
    print(f"Has the number {number_to_count} occurred {count} times")
