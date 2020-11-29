import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from frames import ChannelPlot, BottomBar, TopBar
from pathlib import Path
from utilities import plot_functions as plf


class BrainWave(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1100x800")
        self.title("BrainWave")
        self.minsize(960, 500)
        self.columnconfigure(1, weight=1)

        self.filename = tk.StringVar()
        self.frames = {}

        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.browse_files)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        modelmenu = tk.Menu(self.menubar, tearoff=0)
        modelmenu.add_command(label="Generalized rewiring model", command=self.donothing)
        modelmenu.add_command(label="BrainNet", command=self.donothing)
        modelmenu.add_command(label="SIRS", command=self.donothing)
        modelmenu.add_command(label="Kuramoto", command=self.donothing)
        modelmenu.add_command(label="Machine Learning", command=self.donothing)
        self.menubar.add_cascade(label="Model", menu=modelmenu)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        top_bar = TopBar(self, container)
        top_bar.grid(row=0, column=0, columnspan=2, sticky="EW")
        self.frames[TopBar] = top_bar

        plot_frame = ChannelPlot(self, container)
        plot_frame.grid(row=1, column=0, sticky="EW")
        self.frames[ChannelPlot] = plot_frame

        bottom_bar = BottomBar(self, container)
        bottom_bar.grid(row=2, column=0, sticky="EW")
        self.frames[BottomBar] = bottom_bar

    def donothing(self):
        x = 0

    def browse_files(self):
        self.filename = tk.filedialog.askopenfilename(
            initialdir="/",
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
            tk.messagebox.showinfo('File parser error', 'Could not parse input file, please check format:\n {}'.format(e))
        else:
            self.frames[BottomBar].filename_entry.set(Path(self.filename).name)

            plf.update_plot(self.frames[ChannelPlot])

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

        plf.draw_empty_plot(self.frames[ChannelPlot])
