import sys
from enum import Enum


CALCULATION_ERROR = 0.0000001


class IntFuncType(Enum):
    Polynomial1 = 1


def interpolation(x_list, y_list, int_func_type = IntFuncType.Polynomial1):
    if int_func_type == IntFuncType.Polynomial1:
        x_min = min(x_list)
        x_max = max(x_list)
        y_min = min(y_list)
        y_max = max(y_list)
        for index in range(len(x_list)):
            if abs(x_list[index] - x_min) < CALCULATION_ERROR:
                y_min = y_list[index]
            elif abs(x_list[index] - x_max) < CALCULATION_ERROR:
                y_max = y_list[index]
        a = (y_max - y_min) / (x_max - x_min)
        y_0 = y_min
        x_b = -x_min
        y_b = a * x_b
        b = y_0 + y_b
        return f"{a} * x + {b}"
    else:
        return ""
