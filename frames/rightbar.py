import tkinter as tk
from tkinter import ttk


class RightBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        rightbar_container = ttk.Frame(self)

        rightbar_container.grid(row=1, column=0, sticky="NS")

        top_label = ttk.Label(rightbar_container, text="Sensitivity: ")
        top_label.grid(row=0, column=0, sticky='EW', padx=2)

        for x in range(1):
            tk.Grid.columnconfigure(rightbar_container, x, weight=1)
