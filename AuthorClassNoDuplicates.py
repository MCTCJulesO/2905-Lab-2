# Part 2: Author class - no duplicate books

# Start with the program from part 1.

# In this version, an author can't publish two books with the same name.

# When the publish method is called, print an error message if the book given has the same name as a book currently in the books list. (In other words, make sure the Author object's book list doesn't already contain that name).  

# In your breakout rooms: there's more than one way to solve this - can you come up with two different solutions?

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def publish(self, title):
        if title in self.books:
            print(f"Error: {title} has already been published by {self.name}")
        else:
            self.books.append(title)
    
    def __str__(self):
        book_titles = ', '.join(self.books)
        return f"Author: {self.name}, Books: {book_titles}"

def main():
    author1 = Author("John Smith")
    author2 = Author("Jane Doe")

    author1.publish("Harry Potter")
    author1.publish("Star Wars")
    author2.publish("Resident Evil")
    author1.publish("Harry Potter") # this will print an error message
    author2.publish("Resident Evil") # this will print an error message

    print(author1)
    print(author2)

if __name__ == "__main__":
    main()