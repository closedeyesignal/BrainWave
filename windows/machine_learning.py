import tkinter as tk


class MachineLearning(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Machine Learning")
        self.minsize(400, 300)

        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Import data", command=self.donothing)
        filemenu.add_command(label="Export data", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=self.destroy)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def donothing(self):
         x = 0
