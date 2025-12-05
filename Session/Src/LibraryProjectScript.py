class Medium:
    def __init__(self, publisher, title, year, genre, pages):
        self.publisher = publisher
        self.title = title
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.year}), {self.genre}, {self.pages} stran"


class Book(Medium):
    def __init__(self, publisher, title, year, genre, pages, author):
        super().__init__(publisher, title, year, genre, pages)
        self.author = author

    def __str__(self):
        return f"Kniha: {self.title} - {self.author} ({self.year})"


class Magazin(Medium):
    def __init__(self, publisher, title, year, genre, pages, periodicity):
        super().__init__(publisher, title, year, genre, pages)
        self.periodicity = periodicity

    def __str__(self):
        return f"Časopis: {self.title} ({self.periodicity})"


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.magazines = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [b for b in self.books if b.title != title]

    def add_magazine(self, magazine: Magazin):
        self.magazines.append(magazine)

    def remove_magazine(self, title: str):
        self.magazines = [m for m in self.magazines if m.title != title]

    def __len__(self):
        return len(self.books) + len(self.magazines)

    def __str__(self):
        return f"Knihovna {self.name}, {self.address}"


# ----------------------------------------
# TEST KÓDU
# ----------------------------------------

if __name__ == "__main__":
    lib = Library("Městská Knihovna", "Praha 1")

    b1 = Book("XYZ", "Python pro začátečníky", 2020, "IT", 350, "Novák")
    b2 = Book("ABC", "Harry Potter", 1998, "Fantasy", 500, "J.K. Rowling")

    m1 = Magazin("MediaPress", "Forbes", 2023, "Business", 80, "měsíčně")

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_magazine(m1)

    print("Počet médií:", len(lib))
    print(b1)
    print(m1)