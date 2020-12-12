from frames import BrainWave
import tkinter as tk

root = BrainWave()
root.config(menu=root.menubar)

tk.Grid.rowconfigure(root, 0, weight=0)
tk.Grid.rowconfigure(root, 1, weight=1)
tk.Grid.rowconfigure(root, 2, weight=0)
tk.Grid.columnconfigure(root, 0, weight=0)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 2, weight=0)

root.mainloop()