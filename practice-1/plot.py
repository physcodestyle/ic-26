def print_plot_1d(function, x_min, x_max, point_count):
    dx = (x_max - x_min) / point_count
    for i in range(point_count):
        x = x_min + dx * i
        y = function(x)
        point = ' ' * int(y) + '·'
        print(point)


def func_factory(input_string):
    def func(x):
        return eval(input_string)
    return func


input_string = input("Введите функцию: ")
min = int(input("Введите нижний предел области определения: "))
max = int(input("Введите верхний предел области определения: "))
points = int(input("Введите количество точек в графике: "))
print_plot_1d(func_factory(input_string), min, max, points)
