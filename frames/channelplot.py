from tkinter import ttk
from utilities import plot_functions as plf


class ChannelPlot(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.container = ttk.Frame(self)
        self.container.grid(row=1, column=0, sticky="EW")

        self.canvas = []
        self.plot_list = []
        self.plot_data = []

        plf.draw_empty_plot(self)
