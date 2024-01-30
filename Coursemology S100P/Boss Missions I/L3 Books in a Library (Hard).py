import pickle
import os

class Book:
    def __init__(self, title, fiction=False, borrowed=False):
        self.title = title
        self.fiction = fiction
        self.borrowed = borrowed

class Newspaper(Book):
    def __init__(self, title, publisher, date_of_issue):
        super().__init__(title, fiction=False)
        self.publisher = publisher
        self.date_of_issue = date_of_issue

class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, fiction=True)
        self.author = author
        self.genre = genre

class Comic(Book):
    def __init__(self, title, author, category):
        super().__init__(title, fiction=True)
        self.author = author
        self.category = category

class Biography(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, fiction=False)
        self.author = author
        self.subject = subject

def load_library():
    try:
        with open("library.pkl", "rb") as file:
            library = pickle.load(file)
    except (FileNotFoundError, EOFError):
        library = []
    return library

def save_library(library):
    with open("library.pkl", "wb") as file:
        pickle.dump(library, file)

def display_books(library):
    if not library:
        print("No books in the library.")
    else:
        print("\nLibrary Books:")
        for i, book in enumerate(library, 1):
            fiction_status = "Fiction" if book.fiction else "Non-Fiction"
            borrowed_status = "Borrowed" if book.borrowed else "Available"
            print(f"{i}. {book.title} - {fiction_status} - {borrowed_status}")

def add_book(library, book):
    library.append(book)
    save_library(library)
    print(f"Book '{book.title}' added to the library.")

def remove_book(library, index):
    try:
        removed_book = library.pop(index - 1)
        save_library(library)
        print(f"Book '{removed_book.title}' removed from the library.")
    except IndexError:
        print("Invalid index. No book removed.")

def update_book(library, index, updated_book):
    try:
        library[index - 1] = updated_book
        save_library(library)
        print(f"Book '{updated_book.title}' updated in the library.")
    except IndexError:
        print("Invalid index. No book updated.")

def borrow_book(library, index):
    try:
        book = library[index - 1]
        if not book.borrowed:
            book.borrowed = True
            save_library(library)
            print(f"Book '{book.title}' marked as borrowed.")
        else:
            print("This book is already borrowed.")
    except IndexError:
        print("Invalid index. Cannot borrow the book.")

def return_book(library, index):
    try:
        book = library[index - 1]
        if book.borrowed:
            book.borrowed = False
            save_library(library)
            print(f"Book '{book.title}' marked as returned.")
        else:
            print("This book is not currently borrowed.")
    except IndexError:
        print("Invalid index. Cannot return the book.")

def main():
    library = load_library()

    while True:
        print("\nLibrary Menu:")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Update Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("E. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "1":
            os.system('cls')
            display_books(library)

        elif choice == "2":
            os.system('cls')
            book_type = input("Enter the type of book (Newspaper/Novel/Comic/Biography): ").capitalize()
            title = input("Enter the title of the book: ")

            if book_type == "Newspaper":
                publisher = input("Enter the publisher: ")
                date_of_issue = input("Enter the date of issue: ")
                new_book = Newspaper(title, publisher, date_of_issue)

            elif book_type == "Novel":
                author = input("Enter the author: ")
                genre = input("Enter the genre: ")
                new_book = Novel(title, author, genre)

            elif book_type == "Comic":
                author = input("Enter the author: ")
                category = input("Enter the category: ")
                new_book = Comic(title, author, category)

            elif book_type == "Biography":
                author = input("Enter the author: ")
                subject = input("Enter the subject: ")
                new_book = Biography(title, author, subject)

            else:
                print("Invalid book type. Please enter Newspaper, Novel, Comic, or Biography.")
                continue
            add_book(library, new_book)

        elif choice == "3":
            os.system('cls')
            display_books(library)
            if library:
                index = int(input("Enter the index of the book to remove: "))
                remove_book(library, index)

        elif choice == "4":
            os.system('cls')
            display_books(library)
            if library:
                index = int(input("Enter the index of the book to update: "))
                updated_title = input("Enter the new title: ")
                updated_book_type = input("Enter the new book type (Newspaper/Novel/Comic/Biography): ").capitalize()
                
                if updated_book_type == "Newspaper":
                    publisher = input("Enter the new publisher: ")
                    date_of_issue = input("Enter the new date of issue: ")
                    updated_book = Newspaper(updated_title, publisher, date_of_issue)

                elif updated_book_type == "Novel":
                    author = input("Enter the new author: ")
                    genre = input("Enter the new genre: ")
                    updated_book = Novel(updated_title, author, genre)

                elif updated_book_type == "Comic":
                    author = input("Enter the new author: ")
                    category = input("Enter the new category: ")
                    updated_book = Comic(updated_title, author, category)

                elif updated_book_type == "Biography":
                    author = input("Enter the new author: ")
                    subject = input("Enter the new subject: ")
                    updated_book = Biography(updated_title, author, subject)

                else:
                    print("Invalid book type. Please enter Newspaper, Novel, Comic, or Biography.")
                    continue
                update_book(library, index, updated_book)

        elif choice == "5":
            os.system('cls')
            display_books(library)
            if library:
                index = int(input("Enter the index of the book to borrow: "))
                borrow_book(library, index)

        elif choice == "6":
            os.system('cls')
            display_books(library)
            if library:
                index = int(input("Enter the index of the book to return: "))
                return_book(library, index)

        elif choice == "E":
            print("Exiting Library.\n")
            break
        else:
            print("Invalid choice. Please try again.")

main()