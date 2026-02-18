from lesson10.workshop.DataStore import DataStore


# Decorator to log operations on dictionary
def log_operation(func):
    def wrapper(*args, **kwargs):  # args - variable (different) amount of arguments
        print(f"Executing: {func.__name__} with args={args[1:]}, kwargs={kwargs}")  # print log message
        return func(*args, *kwargs)  # Execute the function

    return wrapper


class LoggingDataStore(DataStore):  # Derived class with extra logs

    @log_operation
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    @log_operation
    def __getitem__(self, key):
        return super().__getitem__(key)
