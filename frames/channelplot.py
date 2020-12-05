from tkinter import ttk
from utilities import plot_functions as plf
import tkinter as tk


class ChannelPlot(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.container = ttk.Frame(self)
        self.container.grid(row=1, column=0, sticky="NSEW")
        tk.Grid.rowconfigure(self.container, 0, weight=1)
        tk.Grid.columnconfigure(self.container, 0, weight=1)

        self.canvas = []
        self.plot_list = []
        self.plot_data = []

        plf.draw_empty_plot(self)
