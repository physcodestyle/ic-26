import sys


def import_data(filename, delimiter):
    try:
        with open(filename, "r") as f:
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
                    key_value_dictionary[keys[j]] = cells[j]
                    length = len(cells[j])
                    if length > max_cell_length:
                        max_cell_length = length
                key_values.append(key_value_dictionary)
            return {
                "keys": keys,
                "rows": rows,
                "dict": key_values,
                "cell_width": max_cell_length,
            }
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
        return None


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


def run():
    data_file = sys.argv[1]
    data = import_data(data_file, ',')
    print_table(data)


run()
