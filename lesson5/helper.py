TPL_FORMAT = "Hello {}"

def print_hello(firstname)
    print(TPL_FORMAT.format(firstname))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5
