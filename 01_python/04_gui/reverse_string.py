#!/usr/bin/env python3
""" Tkinter GUI to reverse inputted text """

from tkinter import Tk, Label, Button, Entry


def updateResultLabel(result_label, entry):
    """ Update the result label """
    text = entry.get()
    result_label.config(text=text[::-1])


if __name__ == '__main__':
    root = Tk()
    root.title('Reverse String')
    root.geometry('300x100')

    label1 = Label(root, text='Enter text:')
    label2 = Label(root, text='')

    entry1 = Entry(root)
    entry1.bind('<Return>', lambda _: updateResultLabel(label2, entry1))

    btn1 = Button(root, text='Reverse',
                  command=lambda: updateResultLabel(label2, entry1))

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=1)

    entry1.grid(row=0, column=1)
    btn1.grid(row=3, column=1)

    # auto focus the entry field on start
    entry1.focus_set()

    root.mainloop()
