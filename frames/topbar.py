import tkinter as tk
from tkinter import ttk

class TopBar(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure()

        topbar_container = ttk.Frame(self)

        topbar_container.grid(row=0, column=0, sticky="EW")

        quit_button = ttk.Button(
            topbar_container,
            text="Quit",
            command=parent.quit,
            cursor="hand2"
        )

        quit_button.grid(row=0, column=0, sticky="EW",padx=2)

        open_button = ttk.Button(
            topbar_container,
            text="Open",
            command=parent.browse_files,
            cursor="hand2"
        )

        open_button.grid(row=0, column=1, sticky="EW", padx=2)

        clear_button = ttk.Button(
            topbar_container,
            text="Clear",
            command=parent.donothing,
            cursor="hand2"
        )

        clear_button.grid(row=0, column=2, sticky="EW", padx=2)

        deselect_button = ttk.Button(
            topbar_container,
            text="Deselect all",
            command=parent.donothing,
            cursor="hand2"
        )

        deselect_button.grid(row=0, column=3, sticky="EW", padx=2)

        select_button = ttk.Button(
            topbar_container,
            text="Select all",
            command=parent.donothing,
            cursor="hand2"
        )

        select_button.grid(row=0, column=4, sticky="EW", padx=2)

        self.showMarker = tk.IntVar(value=1)
        show_marker_check_button = ttk.Checkbutton(
            topbar_container,
            text="Show markers",
            variable=self.showMarker
        )

        show_marker_check_button.grid(row=0, column=5, sticky="EW", padx=2)

        self.muteChannel = tk.IntVar(value=0)
        mute_check_button = ttk.Checkbutton(
            topbar_container,
            text="Mute",
            variable=self.muteChannel
        )

        mute_check_button.grid(row=0, column=6, sticky="EW", padx=2)

        self.selected_availableEpochLengths = tk.StringVar(value="4096")
        epoch_combobox = ttk.Combobox(
            topbar_container,
            textvariable=self.selected_availableEpochLengths,
            state='readonly'
        )
        epoch_combobox["values"] = ("4096", "2048", "1024", "512", "256", "128", "64")
        epoch_combobox.grid(row=0, column=7, sticky="EW", padx=2)
        epoch_combobox.configure(width=5)
        #have to bind the combobox

        epoch_text_label = ttk.Label(topbar_container, text="Epoch length")
        epoch_text_label.grid(row=0, column=8, sticky="EW", padx=2)

        filter_button = ttk.Button(
            topbar_container,
            text="Filter",
            command=parent.donothing,
            cursor="hand2"
        )

        filter_button.grid(row=0, column=9, sticky="EW", padx=2)

        low_freq_filter_textfield = tk.Text(topbar_container)
        low_freq_filter_textfield.configure(height=1, width=4)
        low_freq_filter_textfield.insert("1.0", "0.5")
        low_freq_filter_textfield.grid(row=0, column=10, sticky="EW", padx=2)

        low_freq_filter_textlabel = ttk.Label(topbar_container, text="LF Filter")
        low_freq_filter_textlabel.grid(row=0, column=11, sticky="EW", padx=2)

        high_freq_filter_textfield = tk.Text(topbar_container)
        high_freq_filter_textfield.configure(height=1, width=4)
        high_freq_filter_textfield.insert("1.0", "70.0")
        high_freq_filter_textfield.grid(row=0, column=12, sticky="EW", padx=2)

        high_freq_filter_textlabel = ttk.Label(topbar_container, text="HF Filter")
        high_freq_filter_textlabel.grid(row=0, column=13, sticky="EW", padx=2)