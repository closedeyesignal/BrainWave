import tkinter as tk
from tkinter import ttk


class LeftBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        leftbar_container = ttk.Frame(self)

        leftbar_container.grid(row=1, column=0, sticky="NS")

        top_label = ttk.Label(leftbar_container, text="mean Sync")
        top_label.grid(row=0, column=0, sticky='EW', padx=2)

        for x in range(1):
            tk.Grid.columnconfigure(leftbar_container, x, weight=1)