class Book:
    name: str
    pages: int
    author: str
    publishing: str
    year: str

    def info(self):
        print("hello", id(self))



book1 = Book()
book1.name = "The Stranger"
book1.pages = 245
book1.author = "Albert Camo"
book1.publishing = "Unknown"
book1.year = "1950"
book1.info()        

book2 = Book()
book2.name = "Animal Farm"
book2.pages = 125
book2.author = "George Orwell"
book2.publishing = "Unknown"
book2.year = "1945"
book2.info()

