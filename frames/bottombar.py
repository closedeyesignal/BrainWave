import tkinter as tk
from tkinter import ttk


class BottomBar(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.filename_entry = tk.StringVar()
        self.filename_entry.set("")
        self.epoch_selection = tk.StringVar()
        self.epoch_selection.set("1")
        self.number_of_channels = tk.StringVar()
        self.number_of_channels.set("5")
        self.epoch_requested = tk.StringVar()
        self.epoch_requested.set("20")

        bottombar_container = ttk.Frame(self)

        bottombar_container.grid(row=2, column=0, sticky="EW")

        file_label = ttk.Label(bottombar_container, text="Filename:")
        file_label.grid(row=0, column=0, sticky="EW", padx=2)

        self.file_textfield = tk.Entry(bottombar_container, textvariable=self.filename_entry)
        self.file_textfield.configure(width=20)
        self.file_textfield["state"] = "disabled"
        self.file_textfield.grid(row=0, column=1, sticky="EW", padx=2)

        epoch_label = ttk.Label(bottombar_container, text="Epoch:")
        epoch_label.grid(row=0, column=2, sticky='EW', padx=2)

        self.epoch_textfield = tk.Entry(bottombar_container, textvariable=self.epoch_selection)
        self.epoch_textfield.configure(width=3)
        self.epoch_textfield["state"] = "disabled"
        self.epoch_textfield.grid(row=0, column=3, sticky="EW", padx=2)

        double_back_button = ttk.Button(
            bottombar_container,
            text="<<",
            command=parent.donothing,
            cursor="hand2"
        )

        double_back_button.grid(row=0, column=4, sticky="EW", padx=2)

        back_button = ttk.Button(
            bottombar_container,
            text="<",
            command=parent.donothing,
            cursor="hand2"
        )

        back_button.grid(row=0, column=5, sticky="EW", padx=2)

        fwd_button = ttk.Button(
            bottombar_container,
            text=">",
            command=parent.donothing,
            cursor="hand2"
        )

        fwd_button.grid(row=0, column=6, sticky="EW", padx=2)

        double_fwd_button = ttk.Button(
            bottombar_container,
            text=">>",
            command=parent.donothing,
            cursor="hand2"
        )

        double_fwd_button.grid(row=0, column=7, sticky="EW", padx=2)

        go_to_button = ttk.Button(
            bottombar_container,
            text="go to:",
            command=parent.donothing,
            cursor="hand2"
        )

        go_to_button.grid(row=0, column=8, sticky="EW", padx=2)

        epoch_requested_spin_box = tk.Spinbox(
            bottombar_container,
            from_=0,
            to=30,
            textvariable=self.epoch_requested,
            wrap=False,
            state='readonly'
        )

        epoch_requested_spin_box.config(width=5)
        epoch_requested_spin_box.grid(row=0, column=9, sticky="ew", padx=2)

        channel_label = ttk.Label(bottombar_container, text="Number of channels:")
        channel_label.grid(row=0, column=10, sticky='EW', padx=2)

        self.channel_textfield = tk.Entry(bottombar_container, textvariable=self.number_of_channels)
        self.channel_textfield.configure(width=4)
        self.channel_textfield["state"] = "disabled"
        self.channel_textfield.grid(row=0, column=11, sticky="EW", padx=2)