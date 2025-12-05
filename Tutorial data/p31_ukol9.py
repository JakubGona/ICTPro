"""
Definujte třídu Medium ("rodič" následujících tříd)
- publisher
- title
- year
- genre
- pages

Definujte třídu Book jako potomka třídy Medium
- author

Definujte třídu Magazin jako potomka třídy Medium
- periodicity (měsíčně, čtvrtletně, ročně, týdně...)

Definujte třídu Library
- name
- address
- books (list)
- magazines (list)
+ add_book()
+ remove_book()
+ add_magazine()
+ remove_magazine
+ __len__ vrací počet všech médií v knihovně (počet knih + počet časopisů)
"""
import datetime


class Medium:
    def __init__(self, publisher: str, title: str, year: int, genre: str, pages: int):
        self.publisher = publisher
        self.title = title
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return (f"Medium("
                f"publisher={self.publisher}, "
                f"title={self.title}, "
                f"year={self.year}, "
                f"genre={self.genre}, "
                f"pages={self.pages})")

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self._publisher = publisher.strip().capitalize()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title.strip().capitalize()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        if year <= datetime.date.today().year:
            self._year = year
        else:
            raise ValueError("Rok vydání nesmí být v budoucnosti")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if pages > 0:
            self._pages = pages
        else:
            raise ValueError("Počet stran musí být kladný")


class Book(Medium):
    def __init__(self, publisher: str, title: str, year: int, genre: str, pages: int, author: str):
        super().__init__(publisher, title, year, genre, pages)
        self.author = author

    def __repr__(self):
        return f"Book({super}, author={self.author})"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author.strip().capitalize()


class Magazine(Medium):
    def __init__(self, publisher: str, title: str, year: int, genre: str, pages: int, periodicity: str):
        super().__init__(publisher, title, year, genre, pages)
        self.periodicity = periodicity

    def __repr__(self):
        return f"Magazine({super}, author={self.periodicity})"


class Library:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.books = []
        self.magazines = []

    def __repr__(self):
        return f"Library(name={self.name}, address={self.address})"

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_magazine(self, magazine):
        self.magazines.append(magazine)

    def remove_magazine(self, magazine):
        self.magazines.remove()

    def __len__(self):
        return len(self.books) + len(self.magazines)

book1 = Book("   Albatros", " hlava 22", 1990, "Drama", 350, author="Heller")

if __name__ == "__main__":
    library = Library("MZK", "Lidická 5, Brno")
    library.add_book(Book("   Albatros", " hlava 22", 1990, "Drama", 350, author="Heller"))
    library.add_book(Book("   ikarus", "Harry Potter a kámen mudrců", 1999, "Fantazy",
                          175, "J. K. Rowling"))
    library.add_magazine(Magazine("ABC Publishing", "ABC", 2025, "Technická",
                                  64, "měsíčně"))

    print(f"Knihovna {library} obsahuje {len(library)} knih a časopisů.")
    print("Seznam knih:")
    for book in library.books:
        print(book)
    print("Seznam časopisů:")
    for magazine in library.magazines:
        print(magazine)

    try:
        book1 = Book("AA publisher", " pokus ", 2030, "", 10, "")
        print(book1)
    except Exception as e:
        print(e)

    try:
        book1 = Book("AA publisher", " pokus ", 2020, "", -10, "")
        print(book1)
    except Exception as e:
        print(e)
