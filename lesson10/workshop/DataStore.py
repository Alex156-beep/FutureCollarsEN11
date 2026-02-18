from datetime import datetime


class DataStore:
    def __init__(self, name, description="No description"):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def items(self):
        return self._data.items()

    def __str__(self):
        return f"DataStore(name={self.name}, description={self.description}, created_at={self.created_at}, size={len(self._data)})"
