#!/usr/bin/env python3
""" Draw gauge GUI using tkinter """

from tkinter import Tk, Canvas, Scale, IntVar


def clamp(value, min_value, max_value):
    """ Clamp a value between a minimum and maximum values """
    return max(min_value, min(value, max_value))


def mapValue(value, in_min, in_max, out_min, out_max):
    """ Map a value from one range to another """
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == "__main__":
    root = Tk()
    root.title("Gauge GUI")
    root.geometry("400x300")

    value = IntVar(root, 0)

    canvas = Canvas(root, width=400, height=200, bg="grey")

    coord = 100, 50, 300, 200
    canvas.create_arc(coord, start=30, extent=20,
                      style="arc", outline="red", width=30)
    canvas.create_arc(coord, start=50, extent=20,
                      style="arc", outline="yellow", width=30)
    canvas.create_arc(coord, start=70, extent=80,
                      style="arc", outline="green", width=30)

    canvas.create_text(100, 100, text="0%")
    canvas.create_text(300, 100, text="100%")

    needle = canvas.create_arc(coord, start=90, extent=1, width=3)

    scale = Scale(root, from_=0, to=100, variable=value,
                  orient="horizontal", length=200)

    canvas.pack()
    scale.pack(pady=20)

    def update():
        angle = mapValue(clamp(value.get(), 0, 100), 0, 100, 149, 30)
        canvas.itemconfig(needle, start=angle)

    value.trace_add("write", lambda *_: update())
    canvas.after(400, update)

    root.mainloop()
