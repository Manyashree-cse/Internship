class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class Novel(Book):
    def __init__(self, title, author, genre):
        self.genre=genre
        super().__init__(title, author)

    def details(self):
        return f"'{self.title}' by {self.author} is a {self.genre} novel."

class Magazine(Book):
    def __init__(self, title, author, issue):
        self.issue=issue
        super().__init__(title, author)

    def details(self):
        return f"'{self.title}' by {self.author}, Issue: {self.issue}."

n1 = Novel("The Alchemist", "Paulo Coelho", "Fiction")
print( n1.details())