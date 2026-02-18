import os


def bordered(callback):
    def retfunc():
        w, h = os.get_terminal_size()
        print("=" * w, end="\n \n")
        callback()  # Execute the function
        print()
        print("=" * w, end="\n \n")

    return retfunc


@bordered
def main_func():
    print("Line 1")
    print("Line 2")


@bordered
def other_func():
    print("Line 3")
    print("Line 4")


if __name__ == "__main__":
    main_func()
    other_func()