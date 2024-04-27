from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n {book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book) -> str:
        return self.formatter.format(book)


book = Book("a", "a", "some content")
pa = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(pa.get_book(book))
print(pb.get_book(book))
