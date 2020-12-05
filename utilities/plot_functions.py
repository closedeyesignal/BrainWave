from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.patheffects as pe
import numpy as np


def draw_empty_plot(frame):
    # the figure that will contain the plot
    fig = Figure(dpi=100)
    fig.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.99, wspace=0, hspace=0)

    # adding the subplot
    frame.plot_list = fig.add_subplot(111)
    frame.plot_list.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelleft=False,
        labelbottom=False)
    frame.plot_list.spines['top'].set_visible(False)
    frame.plot_list.spines['right'].set_visible(False)
    frame.plot_list.spines['bottom'].set_visible(False)
    frame.plot_list.spines['left'].set_visible(False)

    frame.canvas = FigureCanvasTkAgg(fig, master=frame.container)
    frame.canvas.draw()
    frame.canvas.get_tk_widget().grid(row=0, column=0, sticky="NSEW")


def update_plot(frame, number_of_channels):
    temp_data, colours = process_plot_data(frame.plot_data, number_of_channels)
    frame.plot_list.plot(temp_data)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=None, hspace=None)

    for i, j in enumerate(frame.plot_list.lines):
        j.set_color(colours[i])

    for i in range(number_of_channels):
        text_string = "Ch. {}".format(i+1)
        frame.plot_list.text(0.05, temp_data[0, i], text_string,
                             ha='center', size=10, color='blue',
                             path_effects=[pe.withStroke(linewidth=5, foreground='w')])

    frame.canvas.draw()


def process_plot_data(channel_data, number_of_channels):
    temp_data = np.array(channel_data)
    norm_data = np.max(np.abs(temp_data), axis=0)
    temp_data = np.divide(temp_data, norm_data,
                          out=np.zeros(temp_data.shape, dtype=float),
                          where=norm_data!=0)

    offset = 0
    colours = ['k'] * number_of_channels
    for x in reversed(range(number_of_channels)):
        if not temp_data[:, x].any():
            colours[x] = 'r'
        temp_data[:, x] += 2 * offset
        offset += 1

    return temp_data, colours
