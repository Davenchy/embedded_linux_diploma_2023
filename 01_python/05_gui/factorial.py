#!/usr/bin/env python3
""" A factorial GUI app """

from tkinter import Tk, Label, Button, Entry


def factorial(n):
    """ Returns the factorial of n """
    return 1 if n == 0 else n * factorial(n - 1)


def calculate(entry, result_label):
    """ Calculate button handler """
    try:
        n = int(entry.get())  # get the entry value
        result = factorial(n)  # calculate the factorial
        # update the result label with the result value
        result_label.config(text=f"The factorial of {n} is {result}")
    except ValueError:
        # handle invalid input
        result_label.config(text="Invalid input!")


if __name__ == '__main__':
    root = Tk()
    root.title('Factorial')
    root.geometry('300x100')

    label1 = Label(root, text='Enter value of integer N:')
    result_label = Label(root, text='')

    entry1 = Entry(root)
    # handle on Enter key pressed while entry is focused
    entry1.bind('<Return>', lambda _: calculate(entry1, result_label))

    btn1 = Button(root, text='Calculate',
                  command=lambda: calculate(entry1, result_label))

    label1.grid(row=0, column=0)
    result_label.grid(row=1, column=1)

    entry1.grid(row=0, column=1)
    btn1.grid(row=3, column=1)

    # auto focus the entry field on start
    entry1.focus_set()

    root.mainloop()
