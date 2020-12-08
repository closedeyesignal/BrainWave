import tkinter as tk
import os
from tkinter import filedialog, messagebox
from frames import ChannelPlot, BottomBar, TopBar, LeftBar, RightBar
from pathlib import Path
from utilities import plot_functions as plf


class BrainWave(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x600")
        self.title("BrainWave")
        self.minsize(1000, 500)

        self.filename = tk.StringVar()
        self.frames = {}

        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.browse_files)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        top_bar = TopBar(self)
        top_bar.grid(row=0, column=0, columnspan=3, sticky="EW")
        top_bar.columnconfigure(0, weight=1)
        top_bar.rowconfigure(0, weight=0)
        self.frames[TopBar] = top_bar

        left_bar = LeftBar(self)
        left_bar.grid(row=1, column=0, sticky="NS")
        left_bar.columnconfigure(0, weight=0)
        left_bar.rowconfigure(1, weight=1)
        self.frames[LeftBar] = left_bar

        plot_frame = ChannelPlot(self)
        plot_frame.grid(row=1, column=1, sticky="NSEW")
        plot_frame.columnconfigure(1, weight=1)
        plot_frame.rowconfigure(1,  weight=1)
        self.frames[ChannelPlot] = plot_frame

        right_bar = RightBar(self)
        right_bar.grid(row=1, column=2, sticky="NS")
        right_bar.columnconfigure(2, weight=0)
        right_bar.rowconfigure(1, weight=1)
        self.frames[RightBar] = right_bar

        bottom_bar = BottomBar(self)
        bottom_bar.grid(row=2, column=0, columnspan=3, sticky="EW")
        bottom_bar.columnconfigure(0, weight=1)
        bottom_bar.rowconfigure(2, weight=0)
        self.frames[BottomBar] = bottom_bar

    def donothing(self):
        x = 0

    def browse_files(self):
        self.filename = tk.filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a file",
            filetypes=(("Text files",
                        "*.txt"),
                       ("All files",
                        "*.*"))
        )
        if not self.filename:  # avoids error pop-up if no files are selected
            return

        try:
            self.read_input()
        except Exception as e:
            tk.messagebox.showinfo(
                'File parser error',
                'Could not parse input file, please check format:\n {}'.format(e))
        else:
            self.frames[BottomBar].filename_entry.set(Path(self.filename).name)

            plf.draw_empty_plot(self.frames[ChannelPlot])
            plf.update_plot(self.frames[ChannelPlot], int(self.frames[BottomBar].number_of_channels.get()))

    def read_input(self):

        if self.frames[ChannelPlot].plot_data:  # ensuring data is overwritten
            self.frames[ChannelPlot].plot_data = []

        with open(self.filename) as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                row_data = [int(x) for x in line.split()]
                self.frames[ChannelPlot].plot_data.append(row_data)

            self.frames[BottomBar].number_of_channels.set(str(len(row_data)))

    def clear_plot(self):
        self.frames[ChannelPlot].canvas.get_tk_widget().pack_forget()

        self.frames[BottomBar].number_of_channels.set("0")
        self.frames[BottomBar].filename_entry.set("")
        self.filename = ""

        self.frames[ChannelPlot].plot_data = []

        plf.draw_empty_plot(self.frames[ChannelPlot])

    def update_markers(self):
        if self.frames[TopBar].showMarker.get():
            self.frames[ChannelPlot].plot_markers()
        else:
            self.frames[ChannelPlot].clear_markers()
