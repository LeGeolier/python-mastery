# stock.py
import csv
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
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self.shares

    @shares.setter
    def shares(self, val):
        if not isinstance(val, int):
            raise TypeError("Expected an integer")
        if val < 0:
            raise ValueError("Shares must be >= 0")
        self._shares = val

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, val):
        if not isinstance(val, float):
            raise TypeError("Expected a float")
        if val < 0:
            raise ValueError("Price must be >= 0")
        self._price = val

    def sell(self, nshares):
        self.shares -= nshares


class DStock(Stock):
    _types = (str, int, Decimal)


def print_portfolio(portfolio):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print(("-" * 10 + " ") * 3)
    for row in portfolio:
        print("%10s %10d %10.2f" % (row.name, row.shares, row.price))
