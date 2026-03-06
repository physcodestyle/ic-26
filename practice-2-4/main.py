import sys
from modules.import_data import import_csv_data
from modules.print_data import print_table, print_plot, PlotType


def run():
    data_file = sys.argv[1]
    imported_data = import_csv_data(data_file, ',')
    print_table(data=imported_data)
    print_plot(data=imported_data, plot_type=PlotType.BAR_TYPE)


run()
