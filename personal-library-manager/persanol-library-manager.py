import json 

class BookCollection:
    """ A class to manage a collection of bools, allowing user to store and organize books their reading matrial. """
    def __init__(self): # the constructor
        """ initialize a new book collection with an empty list of books and setup a storage file """
        self.books_list = []
        self.storage_file = "books-data.json"
        self.read_from_storage()

    def read_from_storage(self):
        """ read the books from the storage file .
        If the file does not exist, create an empty list of books collection. """
        try:
            with open(self.storage_file,"r") as f:
                self.books = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def write_to_storage(self):
        """ Store the current book collection in the JSON storage file """
        with open(self.storage_file,'w') as f:
            json.dump(self.books_list,f,indent=4) # indent to make the file more readable , indent mean 4 spaces    

    def add_new_book(self):
        """ add a new book to the collection """
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        book_year = input("Enter the book year: ")
        book_genre = input("Enter the book genre: ")
        is_book_read = (
            input("Have you read the book? (yes/no): ").lower().strip() == "yes"
        )
        new_book = {
            "title":book_title,
            "author":book_author,
            "year":book_year,
            "genre":book_genre,
            "read":is_book_read
        }
        self.books_list.append(new_book)
        self.write_to_storage()
        print(f"Book added successfully! Title: {book_title}.\n")

    def delete_book(self):
        """ Remove a book from the collection using its title. """ 
        book_title = input("Enter the book title: ")

        for book in self.books_list:
            if book["title"].lower() == book_title.lower():   
                self.books_list.remove(book)
                self.write_to_storage()
                print("Book deleted successfully!")
                return
        print("Book not found!\n")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by (title/author)\nEnter your choice: ").lower().strip()
        search_term = input("Enter the search term: ").lower().strip()

        if search_type == "title":
            book_found = (
            book
            for book in self.books_list
            if search_term in book["title"].lower()
        )
        elif search_type == "author":
            book_found = (
            book
            for book in self.books_list
            if search_term in book["author"].lower()
        )        
        else:
            print("Invalid search type! Please enter 'title' or 'author'.\n")
        
        print("Found the following books: \n")

        if book_found:
            for index, book in enumerate(self.books_list,1):
                reading_status = "Read" if book["read"] else "Not Read"
                print(f"{index}. Title: {book["title"]} Author: {book["author"]} Year: {book["year"]} Genre: {book["genre"]} Status: {reading_status}")   
        else:
            print("No books found.\n")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the book title you want to update: \n")

        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                    print("Leave the field empty if you don't want to update it.")
                    book["title"] = input(f"Enter the new book title ({book['title']}): " ) or book["title"]
                    book["author"] = input(f"Enter the new book author ({book["author"]}): ") or book["author"]
                    book["year"] = input(f"Enter the new book year ({book["year"]}): ") or book["year"]
                    book["genre"] = input(f"Enter the new book genre ({book["genre"]}): ") or book["genre"]
                    book["read"] = (
                         input("Have you read the book? (yes/no): ").lower().strip() == "yes"
                    )
                    self.write_to_storage()
                    print(f"Book updated successfully! Title: {book["title"]}\n")
                    return
            print("Book not found!\n")

        
    def show_list_books(self):
        """Display all books in the collection with their details."""

        if not self.books_list:
                print("Your book list is empty.\n")
                return
        print("Your book list:\n")
        for index, book in enumerate(self.books_list,1):
                reading_status = "Read" if book["read"] else "Not Read"
                print(f"{index}. Title: {book["title"]} Author: {book["author"]} Year: {book["year"]} Genre: {book["genre"]} Status: {reading_status}")        
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.books_list)
        read_books = sum(1 for book in self.books_list if book["read"])
        print(f"You have read {read_books} out of {total_books} books.")
        completion_percentage = (
                (read_books / total_books) * 100 if total_books > 0 else 0
            )
        print(f"Total book in collection: {total_books}")
        print(f"Your reading progress is {completion_percentage:.2f}%.\n")
            
    def start_app(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("\n📚 Welcome to Your Book Collection Manager! 📚")
            print("Select an option:")
            print("1. ➕ Add a new book")
            print("2. 🗑️ Delete a book")
            print("3. 🔍 Find a book")
            print("4. ✏️ Update a book")
            print("5. 📖 Show book list")
            print("6. 📊 Show reading progress")
            print("7. 🚪 Exit")
            print("Enter your choice (1-7): ")

            choice = input()
            if   choice == "1":
                self.add_new_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.find_book()
            elif choice == "4":
                self.update_book()
            elif choice == "5":
                self.show_list_books()
            elif choice == "6":
                self.show_reading_progress()
            elif choice == "7":
                self.write_to_storage()
                print("Thank you for using Book Collection Manager. Goodbye! 👋")
                break
            else:
              print("❌ Invalid choice. Please try again.\n")
                
if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.start_app()