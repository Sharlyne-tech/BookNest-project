class Author:
    def __init__(self, id, name, bio):
        self.id = id
        self.name = name
        self.bio = bio


class Book:
    def __init__(self, id, title, genre, author):
        self.id = id
        self.title = title
        self.genre = genre
        self.author = author 
        self.borrowed = False     