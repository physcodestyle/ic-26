import sys


def import_csv_data(filename, delimiter):
    try:
        with open(filename, "r") as f:
            global_max_value = -sys.float_info.max
            global_min_value = sys.float_info.max
            strings = f.read().split("\n")
            keys = strings[0].split(delimiter)
            max_cell_length = 0
            for key in keys:
                length = len(key)
                if length > max_cell_length:
                    max_cell_length = length
            rows = []
            key_values = []
            for i in range(1, len(strings)):
                cells = strings[i].split(delimiter)
                rows.append(cells)
                key_value_dictionary = {}
                for j in range(len(cells)):
                    if float(cells[j]) > global_max_value:
                        global_max_value = float(cells[j])
                    if float(cells[j]) < global_min_value:
                        global_min_value = float(cells[j])
                    key_value_dictionary[keys[j]] = float(cells[j])
                    length = len(cells[j])
                    if length > max_cell_length:
                        max_cell_length = length
                key_values.append(key_value_dictionary)
            return {
                "keys": keys,
                "rows": rows,
                "dict": key_values,
                "cell_width": max_cell_length,
                "extremum": {
                    "max": global_max_value,
                    "min": global_min_value,
                }
            }
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
        return None