#!/usr/bin/env python3
# print the system path env var
import os

print("Your PATH is:")

for value in os.environ['PATH'].split(':'):
    print(value)
