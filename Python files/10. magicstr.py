# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # __repr__ should return a printable representation of the object, most likely one of the ways possible to create this object.
    # See official documentation here. __repr__ is more for developers while __str__ is for end users.
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print each object
print(b1)
print(b2)

# use str() and repr()
print(str(b1))
print(repr(b2))
