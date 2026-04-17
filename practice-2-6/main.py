import sys
from modules.import_data import import_csv_data
from modules.print_data import print_table, print_plot, PlotType
from modules.approximation import approximation, ApproximationFuncType


def run():
    data_file = sys.argv[1]
    data = import_csv_data(filename=data_file, delimiter=",")
    x_data = data["cols"][0]
    y_data = data["cols"][3]
    result = approximation(x_list=x_data, y_list=y_data, approximation_func_type=ApproximationFuncType.Polynomial1)
    print(result)


if __name__ == '__main__':
    run()
