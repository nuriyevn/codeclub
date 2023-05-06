class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    __bookcount = 0
    __booklist = None

    @classmethod
    def getbookcount(cls):
        return cls.__bookcount

    def __init__(self, title, booktype):
        Book.__bookcount += 1
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

    def description(self):
        print(f"title = {self.title} ,  booktype = {self.booktype}")

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

b1 = Book("Kaidasheva simya", "PAPERBACK")
b2 = Book("Eneida", "EBOOK")
b3 = Book("Python Advanced Cookbook", "HARDCOVER")

print(b3)

print(Book.getbooktypes())

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
thebooks.append(b3)

print(b1.getbookcount())
print(b2.getbookcount())
print(b3.getbookcount())

for book in thebooks:
    book.description()


print(Book.getbookcount())


b1.description()




