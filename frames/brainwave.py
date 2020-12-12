import tkinter as tk
import os
from tkinter import filedialog, messagebox
from frames import ChannelPlot, BottomBar, TopBar, LeftBar, RightBar
from pathlib import Path
from utilities import plot_functions as plf
from windows import MachineLearning


class BrainWave(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x600")
        self.title("BrainWave")
        self.minsize(1000, 500)

        self.filename = tk.StringVar()
        self.frames = {}
        self.windows = {}

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


        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Filter", command=self.donothing)
        editmenu.add_command(label="Standard Filter", command=self.donothing)
        editmenu.add_command(label="multiFilter", command=self.donothing)
        editmenu.add_command(label="Envelope", command=self.donothing)
        editmenu.add_command(label="Rank Matrix", command=self.donothing)
        editmenu.add_command(label="Order matrix", command=self.donothing)
        editmenu.add_command(label="Random time", command=self.donothing)
        editmenu.add_command(label="K means", command=self.donothing)
        editmenu.add_command(label="Consensus clusters", command=self.donothing)
        editmenu.add_command(label="Set clusters anat", command=self.donothing)
        editmenu.add_command(label="Set clusters RSN", command=self.donothing)
        editmenu.add_command(label="Reset clusters", command=self.donothing)
        editmenu.add_command(label="Matrix to Buffer", command=self.donothing)
        editmenu.add_command(label="Subtract Buffer", command=self.donothing)
        editmenu.add_command(label="Compare to Buffer", command=self.donothing)
        editmenu.add_command(label="MST to Matrix", command=self.donothing)
        editmenu.add_command(label="MST to Buffer", command=self.donothing)
        editmenu.add_command(label="MST explained", command=self.donothing)
        editmenu.add_command(label="MST unexplained", command=self.donothing)
        editmenu.add_command(label="Clear Buffer", command=self.donothing)
        editmenu.add_command(label="Phase rand surr I", command=self.donothing)
        editmenu.add_command(label="Phase rand surr II", command=self.donothing)
        editmenu.add_command(label="Decouple", command=self.donothing)
        editmenu.add_command(label="Order by frequency", command=self.donothing)
        editmenu.add_command(label="Virtual Reference", command=self.donothing)
        editmenu.add_command(label="Set beginCursor", command=self.donothing)
        editmenu.add_command(label="Set seedChannel", command=self.donothing)
        editmenu.add_command(label="Bin density", command=self.donothing)
        editmenu.add_command(label="Clear", command=self.donothing)
        self.menubar.add_cascade(label="Edit", menu=editmenu)

        analyzemenu = tk.Menu(self.menubar, tearoff=0)
        analyzemenu.add_command(label="FFT", command=self.donothing)
        analyzemenu.add_command(label="Coherence", command=self.donothing)
        analyzemenu.add_command(label="Imag Coh", command=self.donothing)
        analyzemenu.add_command(label="Phase Coh", command=self.donothing)
        analyzemenu.add_command(label="PLI", command=self.donothing)
        analyzemenu.add_command(label="WPLI", command=self.donothing)
        analyzemenu.add_command(label="PLT", command=self.donothing)
        analyzemenu.add_command(label="PTE", command=self.donothing)
        analyzemenu.add_command(label="HVG-TE", command=self.donothing)
        analyzemenu.add_command(label="SL", command=self.donothing)
        analyzemenu.add_command(label="AEC", command=self.donothing)
        analyzemenu.add_command(label="AEC-c", command=self.donothing)
        analyzemenu.add_command(label="Correlation", command=self.donothing)
        analyzemenu.add_command(label="PageRank", command=self.donothing)
        analyzemenu.add_command(label="recPageRank", command=self.donothing)
        analyzemenu.add_command(label="Temporal Networks", command=self.donothing)
        analyzemenu.add_command(label="TCR", command=self.donothing)
        analyzemenu.add_command(label="Weighted Graph", command=self.donothing)
        analyzemenu.add_command(label="Unweighted Graph", command=self.donothing)
        analyzemenu.add_command(label="Cluster analysis", command=self.donothing)
        analyzemenu.add_command(label="Visibility Graph", command=self.donothing)
        analyzemenu.add_command(label="Graph spectral analysis", command=self.donothing)
        analyzemenu.add_command(label="Minimum Spanning Tree", command=self.donothing)
        analyzemenu.add_command(label="Density", command=self.donothing)
        analyzemenu.add_command(label="FDR", command=self.donothing)
        analyzemenu.add_command(label="Batch", command=self.donothing)
        self.menubar.add_cascade(label="Analyze", menu=analyzemenu)

        modelmenu = tk.Menu(self.menubar, tearoff=0)
        modelmenu.add_command(label="Generalized rewiring model", command=self.generalized_rewiring_model_window)
        modelmenu.add_command(label="BrainNet", command=self.brainNet_window)
        modelmenu.add_command(label="SIRS", command=self.sirs_window)
        modelmenu.add_command(label="Kuramoto", command=self.kuramoto_window)
        modelmenu.add_command(label="Machine Learning", command=self.machine_learning_window)
        self.menubar.add_cascade(label="Model", menu=modelmenu)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        top_bar = TopBar(self, container)
        top_bar.grid(row=0, column=0, columnspan=2, sticky="EW")
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

    def machine_learning_window(self):
        if not MachineLearning in self.windows:
            secondary_window = MachineLearning()
            secondary_window.config(menu=secondary_window.menubar)
            self.windows[MachineLearning] = secondary_window

    def sirs_window(self):
        win = tk.Toplevel()
        win.wm_title("SIRS")

    def brainNet_window(self):
        win = tk.Toplevel()
        win.wm_title("BrainNet")

    def kuramoto_window(self):
        win = tk.Toplevel()
        win.wm_title("Kuramoto")

    def generalized_rewiring_model_window(self):
        win = tk.Toplevel()
        win.wm_title("Generalized rewiring model")