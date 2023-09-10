#!/usr/bin/env python3
""" Tkinter GUI to reverse inputted text """

from tkinter import Tk, Button, messagebox


def reply(number):
    """ show a messagebox with the button number """
    messagebox.showinfo('Button Reply', f'You pressed button{number}')


if __name__ == '__main__':
    root = Tk()
    root.title('Buttons Grid')
    root.geometry('240x100')

    btn1 = Button(root, text='Button 1', command=lambda: reply(1))
    btn2 = Button(root, text='Button 2', command=lambda: reply(2))
    btn3 = Button(root, text='Button 3', command=lambda: reply(3))
    btn4 = Button(root, text='Button 4', command=lambda: reply(4))

    btn1.grid(row=0, column=1)
    btn2.grid(row=1, column=0)
    btn3.grid(row=1, column=2)
    btn4.grid(row=2, column=1)

    root.mainloop()
