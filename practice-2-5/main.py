import sys
from modules.import_data import import_csv_data
from modules.print_data import print_table, print_plot, PlotType


def run():
    data_file = sys.argv[1]
    data = import_csv_data(filename=data_file, delimiter=",")
    print_plot(data=data, plot_type=PlotType.GRAPH_TYPE)


if __name__ == '__main__':
    run()
