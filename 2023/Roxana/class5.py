# everything is Object 
# behaviour (method)
# data (attribute, property)

# int, float, str, list, tuple, dict, set
##class Pen:
##    company = ""
##    color = ""
##    capcity = 100
##    def write(self):
##        print("I am writing....")
##        self.capcity -= 1
##
##
##blue_pen = Pen()
##blue_pen.company = "Kian"
##blue_pen.color = "blue"
##blue_pen.write()
import os

def perct_of(value, total_val):
    per = round((value / total_val) * 100, 2)
    return per

def number_of_books():
    books = os.listdir(r"C:\Users\saeed\Documents\Books")
    return len(books)

def number_of_book(book_name):
    books = os.listdir(r"C:\Users\saeed\Documents\Books")
    total = 0
    for book in books:
        if book_name.lower() in book.lower():
            total += 1
    return total



books = ['python', 'csharp', 'php', 'java',
         'html', 'css', 'c plus plus', 'javascript',
         'algorithm', 'database', 'sql', 'android',
         'computer science', 'porgramming', 'django']
for book in books:
    books_total = number_of_books()
    a_book_number = number_of_book(book)
    perc = perct_of(a_book_number, books_total)
    print(f"Number of {book.title()}: {a_book_number}\nPercetages of {book}: {perc}%")
    print('-' * 35)
