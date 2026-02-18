from lesson5.workshop.book import Book


# SERIALIZATION change Object to Text
# DESERIALIZATION Text to Object

def from_file_format(line):  # Map text line to object (DESERIALIZATION)
    title, author, available = line.strip().split('|')
    return Book(title, author, available == 'True')


def load_books_from_file(filename):
    books = []
    try:
        with open(filename) as file:
            for line in file:  # line is String
                books.append(from_file_format(line))
    except FileNotFoundError:
        print("File with books nos exists, creating new file")

    return books


def display_books(books):
    if not books:  # List of Book objects
        print("No books in library")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.describe()}")


def add_book(books, title, author):
    books.append(Book(title, author))
    print(f"Book {title} author {author} has been added")


def save_books_to_file(filename, books):
    with open(filename, 'w') as fd:
        for book in books:  # Book is object
            fd.write(book.to_file_format() + '\n')  # SERIALIZE


def borrow_book(books, book_number):
    # if 0 < book_number and book_number <= len(books):
    if 0 < book_number <= len(books):
        book = books[book_number - 1]
        if book.available:
            book.available = False
            print(f"You borrowed book {book.title}")
        else:
            print("Book is already borrowed")
    else:
        print(f"Book with number {book_number} not exists")


def return_book(books, book_number):
    if 0 < book_number <= len(books):
        book = books[book_number - 1]
        if not book.available:
            book.available = True
            print(f"Returned book: {book.title}")
        else:
            print("Book has not been borrowed")
    else:
        print(f"Book with number {book_number} not exists")


def main():
    filename = "books.txt"
    books = load_books_from_file(filename)  # list books contains objects
    # print(books)

    while True:
        print("\n--- MENU ---")
        print("1. Display all books")
        print("2. Add new book")
        print("3. Borrow a book")
        print("4. Return a previously borrowed book")
        print("5. Exit")

        choice = input("Choose option")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            title = input("Provide book title")
            author = input("Provide book author")
            add_book(books, title, author)
        elif choice == '3':
            display_books(books)
            try:
                book_number = int(input("Provide book number"))
                borrow_book(books, book_number)
            except ValueError:
                print("Wrong number")
        elif choice == '4':
            display_books(books)
            try:
                book_number = int(input("Provide book number"))
                return_book(books, book_number)
            except ValueError:
                print("Wrong number")
        elif choice == '5':
            save_books_to_file(filename, books)
            print("Thanks for using library program")
            break
        else:
            print("Wrong option")


main()