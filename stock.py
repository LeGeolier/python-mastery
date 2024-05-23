# stock.py
import sys
from decimal import Decimal


class Stock:
    _types = (str, int, float)
    __slots__ = ["name", "_shares", "_price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, val):
        if not isinstance(val, int):
            raise TypeError("Expected an integer")
        if val < 0:
            raise ValueError("Shares must be >= 0")
        self._shares = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if not isinstance(val, float):
            raise TypeError("Expected a float")
        if val < 0:
            raise ValueError("Price must be >= 0")
        self._price = val

    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self._shares}, {self._price})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Stock) and (
            (self.name, self._shares, self.price)
            == (other.name, other._shares, other._price)
        )


class DStock(Stock):
    _types = (str, int, Decimal)


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


def print_portfolio(portfolio):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print(("-" * 10 + " ") * 3)
    for row in portfolio:
        print("%10s %10d %10.2f" % (row.name, row.shares, row.price))


class SimpleStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
