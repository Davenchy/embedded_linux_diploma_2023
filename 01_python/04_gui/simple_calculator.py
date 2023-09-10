#!/usr/bin/env python3
""" Simple GUI calculator """

from tkinter import Tk, Frame, Label, Button, Entry, Radiobutton, IntVar
from typing import Callable

""" Operator callback takes two numbers a and b as arguments and
returns the result of the operation as a number """
OperatorCallback = Callable[[int, int], int]

""" Operator definition is a tuple
(Operator Name: str, Template: str, Callback: OperatorCallback)

The template is a string representing the result
The formatting function will be used with the template
template.format(a, b, result) """
OperatorDefinition = tuple[str, str, OperatorCallback]


def calculate(entryA: Entry, entryB: Entry, result_label: Label,
              opDef: OperatorDefinition):
    """ Calculate button handler

    Args:
        entryA (Entry): The first entry
        entryB (Entry): The second entry
        result_label (Label): The result label
        opDef (OperatorDefinition): The operator definition"""

    a, b = None, None

    try:
        a = int(entryA.get())  # get the entry value of a
    except ValueError:
        # handle invalid input
        result_label.config(text="Invalid input of A!")
        return

    try:
        b = int(entryB.get())  # get the entry value of b
    except ValueError:
        # handle invalid input
        result_label.config(text="Invalid input of B!")
        return

    _, template, callback = opDef
    result = callback(a, b)  # calculate the result

    # update the result label with the result value
    result_label.config(text=template.format(a, b, result))


if __name__ == '__main__':
    # define operators
    operators: list[OperatorDefinition] = [
        ('Add', 'The sum of {} and {} is {}', lambda a, b: a + b),
        ('Sub', 'The subtraction of {} and {} is {}', lambda a, b: a - b)
    ]

    root = Tk()
    root.title('Simple Calculator')
    root.geometry('250x130')

    frame1 = Frame(root)

    selectedOperator = IntVar()
    selectedOperator.set(0)

    label1 = Label(root, text='Enter value of A:')
    label2 = Label(root, text='Enter value of B:')
    label3 = Label(root, text='')

    entry1 = Entry(root)
    entry2 = Entry(root)

    # define radio button for each operator
    for i, opDef in enumerate(operators):
        def select(index):
            return lambda _: selectedOperator.set(index)

        Radiobutton(frame1, text=opDef[0],
                    variable=selectedOperator, value=i).pack()
        root.bind(f'<Control-Key-{i + 1}>', select(i))

    def do_calculate():
        calculate(
            entry1, entry2, label3, operators[selectedOperator.get()])

    btn1 = Button(root, text='Calculate', command=do_calculate)

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=2, column=0, columnspan=2)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    btn1.grid(row=3, column=1)
    frame1.grid(row=3, column=0)

    # focus entry1 on start
    entry1.focus_set()
    # focus entry2 on pressing enter while entry1 is focused
    entry1.bind('<Return>', lambda _: entry2.focus_set())
    # calculate result on pressing enter while entry2 is focused
    entry2.bind('<Return>', lambda _: do_calculate())

    root.mainloop()
