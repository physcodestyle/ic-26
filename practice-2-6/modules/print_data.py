from enum import Enum
import sys


class PlotType(Enum):
    BAR_TYPE = 1
    GRAPH_TYPE = 2


MARKERS = ( "░", "▒", "▓", "█" )
EMPTY_POINT = "·"
POINTS = ("⏺", "⊕", "⊗", "⎊", "⍟", "⊛")
WIDTH = 20
HEIGHT = 25


def print_table(data):
    column_width = data["cell_width"]
    header = ''
    for column_index in range(len(data["keys"])):
        cell = data["keys"][column_index]
        for _ in range(len(cell), column_width):
            cell += ' '
        header += '| ' + cell + ' '
    table_width = len(header) + 1
    header = "-" * table_width + '\n' + header + '|\n' + "-" * table_width
    print(header)
    for row_index in range(len(data["rows"])):
        row = ''
        for column_index in range(len(data["keys"])):
            cell = data["rows"][row_index][column_index]
            for _ in range(len(cell), column_width):
                cell += ' '
            row += '| ' + cell + ' '
        print(row + '|')
    print("-" * table_width)


def print_bar_plot(data):
    plot = []
    plot_height = round(data["extremum"]["max"] - data["extremum"]["min"])
    for row_index in range(plot_height + 1):
        row = []
        for group_index in range(len(data["rows"])):
            for bar_index in range(len(data["keys"])):
                current_value = float(data["rows"][group_index][bar_index]) - data["extremum"]["min"]
                if row_index <= round(current_value):
                    row.append(MARKERS[bar_index])
                else:
                    row.append(" ")
            row.append(" ")
        plot.append(row)
    plot.reverse()
    for row in plot:
        print("".join(row))


def print_graph_plot(data):
    x_min = min(data["cols"][0])
    x_max = max(data["cols"][0])
    y_min = sys.float_info.max
    y_max = -sys.float_info.max

    plot = []
    for _ in range(HEIGHT):
        row = []
        for _ in range(WIDTH):
            row.append(f" {EMPTY_POINT} ")
        plot.append(row)            

    for col_index in range(1, len(data["cols"])):
        if min(data["cols"][col_index]) < y_min:
            y_min = min(data["cols"][col_index])
        if max(data["cols"][col_index]) > y_max:
            y_max = max(data["cols"][col_index])

    for col_index in range(1, len(data["cols"])):
        for row_index in range(len(data["cols"][0])):
            x = round((data["cols"][0][row_index] - x_min) * (WIDTH - 1) / (x_max - x_min))
            y = round((data["cols"][col_index][row_index] - y_min) * (HEIGHT - 1) / (y_max - y_min))
            plot[y][x] = f" {POINTS[col_index - 1]} "
    
    plot.reverse()
    for row in plot:
        print("".join(row))

    # point_count = len(data["rows"])
    # dx = (x_max - x_min) / point_count
    # for i in range(point_count + 1):
    #     x = x_min + dx * i
    #     y = function(x)
    #     point = ' ' * int(y) + '·'
    #     print(point)


def print_plot(data, plot_type: PlotType):
    if plot_type == PlotType.BAR_TYPE:
        print_bar_plot(data)
    elif plot_type == PlotType.GRAPH_TYPE:
        print_graph_plot(data)
    else:
        print(f"Error: chosen plot type '{plot_type}' was not found.")
        
