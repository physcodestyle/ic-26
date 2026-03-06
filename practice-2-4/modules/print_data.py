from enum import Enum


class PlotType(Enum):
    BAR_TYPE = 1


MARKERS = ( "░", "▒", "▓", "█" )


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


def print_plot(data, plot_type: PlotType):
    if plot_type == PlotType.BAR_TYPE:
        print_bar_plot(data)
    else:
        print(f"Error: chosen plot type '{plot_type}' was not found.")
        
