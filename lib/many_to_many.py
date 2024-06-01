class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return self._authors


class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string.")
        if not isinstance(royalties, (int, float)):
            raise ValueError("Royalties must be a number.")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.contracts().append(contract)

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string.")
        if not isinstance(royalties, (int, float)):
            raise ValueError("Royalties must be a number.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls.all_contracts if contract.date == date], key=lambda x: x.date)
