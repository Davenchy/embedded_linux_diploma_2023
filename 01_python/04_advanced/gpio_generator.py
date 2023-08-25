#!/usr/bin/env python3
""" Generates a init function of GPIO for AVR in C """

import sys

if __name__ == '__main__':
    filename = "init.c"
    code = """
void Init_PORTA_DIR(void)
{{
    DDRA = 0b{};
}}

"""

    data = ''
    for i in range(8):
        value = input(
            'Enter Bit {} mode(on/1, off/0(default)): '.format(i)).strip()
        value = '1' if value in {'on', '1'} else '0'
        data += value

    with open(filename, 'w') as f:
        f.write(code.format(data))
