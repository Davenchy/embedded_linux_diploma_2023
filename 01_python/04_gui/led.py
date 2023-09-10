#!/usr/bin/env python3
""" LED Controller GUI """

from tkinter import Tk, Button, BooleanVar, Canvas


def btn_msg(led_state: BooleanVar) -> str:
    """ Return a message to display on the button that controls LED state
    Args:
        led_state (BooleanVar): The current state of the LED
    Returns (str) The message"""


if __name__ == '__main__':
    root = Tk()
    root.title("LED Controller")
    root.geometry("100x150")
    root.configure(background="white")

    # define the led state
    led_state = BooleanVar(root, value=False)

    # button to toggle led state
    btn = Button(root, command=lambda: led_state.set(not led_state.get()),
                 text="Turn OFF" if led_state.get() else "Turn ON")

    canvas = Canvas(root, width=100, height=100, bg="white")
    oval = canvas.create_oval(25, 25, 75, 75, width=2,
                              fill='red' if led_state.get() else 'white')

    canvas.pack()
    btn.pack(pady=10)

    # on led state change handler
    def onStateChange(_c, _a, _b):
        state = led_state.get()
        # update button label
        btn.config(text="Turn OFF" if state else "Turn ON")
        # update canvas oval
        canvas.itemconfig(oval, fill='red' if state else 'white')

    # handle led state change
    led_state.trace_add('read', onStateChange)

    root.mainloop()
