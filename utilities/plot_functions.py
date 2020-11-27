from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def draw_empty_plot(frame):
    # the figure that will contain the plot
    fig = Figure(figsize=(9, 7), dpi=100)

    # adding the subplot
    frame.plot_list = fig.add_subplot(111)

    frame.canvas = FigureCanvasTkAgg(fig, master=frame.container)
    frame.canvas.draw()
    frame.canvas.get_tk_widget().pack()


def update_plot(frame):
    frame.plot_list.plot(frame.plot_data)
    frame.canvas.draw()
