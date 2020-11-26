import tkinter as tk
from tkinter import ttk

class ChannelPlot(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure()

        channelplot_container = ttk.Frame(self)

        channelplot_container.grid(row=1, column=0, sticky="EW")