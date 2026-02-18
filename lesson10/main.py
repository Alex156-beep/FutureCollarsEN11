import sys


def avg(*args):
    if not args:
        return 0

    counter = 0
    sum = 0

    for arg in args:
        sum += arg
        counter += 1

    return sum / counter


# def parse_args(argv):
#     if argv[1] == "max":
#         return max(*[float (item) for item in argv[2:]])
#     if argv[1] == "min":
#         return min(*[float(item) for item in argv[2:]])
#     if argv[1] == "avg":
#         return avg(*[float(item) for item in argv[2:]])

def parse_args(argv):
    def aggr_func(func_name):
        if func_name == "max":
            return max
        if func_name == "min":
            return min
        if func_name == "avg":
            return avg

    aggrf = aggr_func(argv[1])
    return aggrf(*[float(item) for item in argv[2:]])  # min/max/avg(*[float(item) for item in argv[2:]])


if __name__ == "__main__":
    result = parse_args(sys.argv)
    print(result)