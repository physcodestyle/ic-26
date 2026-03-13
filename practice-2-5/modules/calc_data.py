def analytic_func_factory(equation):
    def func(x):
        return eval(equation)
    return func


def sequence_factory(values, cycle_body):
    def func(n):
        if n < 0:
            return 0, True
        elif n < len(values):
            return values[n], False
        else:
            result = values
            for i in range(len(values), n):
                result.append(eval(cycle_body))
            return result, False
    return func
