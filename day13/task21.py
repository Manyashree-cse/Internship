class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class IssuedBook(Book):
    def __init__(self, title, author, borrower, date):
        super().__init__(title,author)
        self.borrower=borrower
        self.date=date
    def get_summary(self):
        return f"{self.title} by {self.author} issued to {self.borrower} on {self.date}"

b1 = IssuedBook("HP", "Rowling", "Harry", "2024-01-01")
print( b1.get_summary())