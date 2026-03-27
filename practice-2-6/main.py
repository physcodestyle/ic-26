import sys
from modules.import_data import import_csv_data
from modules.print_data import print_table, print_plot, PlotType
from modules.interpolation import interpolation, IntFuncType


def run():
    data_file = sys.argv[1]
    data = import_csv_data(filename=data_file, delimiter=",")
    x_data = data["cols"][0]
    y_data = data["cols"][3]
    int_func (x_list=x_data, y_list=y_data, int_func_type="IntFuncType.Polynomial1")
    print(int_func)


if __name__ == '__main__':
    run()
