import sys
from enum import Enum
from random import random


CALCULATION_ERROR = 0.0000001
RANDOM_VALUES_COUNT = 100


class ApproximationFuncType(Enum):
    Polynomial1 = 1


def summa_of_differences_1d(x_list, y_list, a):
    s = 0
    for index in range(len(x_list)):
        y = a * x_list[index] + y_list[0]
        s += (y_list[index] - y) * (y_list[index] - y)
    return s


def get_new_a_1d(x_list, y_list, a_start, a_end):
    a_list = []
    min_sum = -sys.float_info.max
    min_index = -1
    for index in range(RANDOM_VALUES_COUNT):
        new_a = abs(a_end - a_start) * random()
        sum = summa_of_differences_1d(x_list=x_list, y_list=y_list, a=new_a)
        if sum < min_sum:
            min_index = index
            min_sum = sum
        a_list.append(new_a)
    return (a_list[min_index], min(a_list), max(a_list))


def approximation(x_list, y_list, approximation_func_type = ApproximationFuncType.Polynomial1):
    if approximation_func_type == ApproximationFuncType.Polynomial1:
        a_start = -sys.float_info.min
        a_end = sys.float_info.min
        a, a_start, a_end = get_new_a_1d(x_list, y_list, a_start, a_end)
        is_approximation_processing = True
        while is_approximation_processing:
            a_old = a
            a_new, a_start, a_end = get_new_a_1d(x_list=x_list, y_list=y_list, a_start=a_start, a_end=a_end)
            is_approximation_processing = not abs(a_new - a_old) < CALCULATION_ERROR
        return f"{a} * x + {y_list[0]}"
    else:
        return ""
