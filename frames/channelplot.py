from tkinter import ttk
from utilities import plot_functions as plf
import tkinter as tk
import inspect


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
        self.markers = []
        self.mouse_marker = []

        plf.draw_empty_plot(self)

    def clear_markers(self):

        for marker in self.markers:
            marker.remove()
            self.canvas.draw()

        self.markers = []

    def plot_markers(self):

        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)

        if not self.plot_data:
            x_length = 1
            number_of_channels = 21
        else:
            x_length = len(self.plot_data)
            number_of_channels = len(self.plot_data[0])

        for x in range(1, 4):
            temp_marker = self.plot_list.plot([x / 4 * x_length, x / 4 * x_length],
                                              [-1, number_of_channels*2 - 1],
                                              color='k')
            for line in temp_marker:
                self.markers.append(line)

        if calframe[1][3] is 'update_markers':
            self.canvas.draw()
