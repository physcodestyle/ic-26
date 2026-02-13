def print_plot_1d(function, x_min, x_max, point_count):
    dx = (x_max - x_min) / point_count
    for i in range(point_count):
        x = x_min + dx * i
        y = function(x)
        point = ' ' * int(y) + '·'
        print(point)


def f(x):
    return x * x


min = 0
max = 10
points = 10


print_plot_1d(f, min, max, points)
