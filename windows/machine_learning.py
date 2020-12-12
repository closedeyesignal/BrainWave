import tkinter as tk


class MachineLearning(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Machine Learning")
        self.minsize(400, 300)
        self.protocol("WM_DELETE_WINDOW", self.destroy_window)

        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Import data", command=self.donothing)
        filemenu.add_command(label="Export data", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=self.destroy_window)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def donothing(self):
         x = 0

    def destroy_window(self):
        self.master.windows.pop(MachineLearning)
        self.destroy()
