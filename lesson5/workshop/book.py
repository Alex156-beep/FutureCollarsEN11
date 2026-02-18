class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def describe(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} - {self.author} ({status})"

    def to_file_format(self):
        return f"{self.title}|{self.author}|{self.available}"