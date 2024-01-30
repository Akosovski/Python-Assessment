class Book:
    def __init__(self, title):
        self.title = title

class Newspaper(Book):
    def __init__(self, title):
        super().__init__(title)
        self.fiction = False

class Novel(Book):
    def __init__(self, title):
        super().__init__(title)
        self.fiction = True