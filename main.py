import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from frames import ChannelPlot, BottomBar, TopBar
from pathlib import Path

class BrainWave(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1100x800")
        self.title("BrainWave")
        self.minsize(960, 500)
        self.columnconfigure(1, weight=1)
        #self.rowconfigure(0, weight=1)

        self.filename = tk.StringVar()
        self.frames = {}

        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.browse_files)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

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

        self.frames[BottomBar].file_textfield.config(state="normal")
        self.frames[BottomBar].file_textfield.delete("1.0", tk.END)
        self.frames[BottomBar].filename_entry = Path(self.filename).name
        self.frames[BottomBar].file_textfield.insert("1.0", self.frames[BottomBar].filename_entry)
        self.frames[BottomBar].file_textfield.config(state="disabled")
        # call frame to update plot


root = BrainWave()
root.config(menu=root.menubar)
root.mainloop()

print(root.filename)