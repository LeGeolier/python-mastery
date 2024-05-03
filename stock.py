# stock.py
import csv
from decimal import Decimal


class Stock:
    types = (str, int, Decimal)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def print_portfolio(portfolio):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print(("-" * 10 + " ") * 3)
    for row in portfolio:
        print("%10s %10d %10.2f" % (row.name, row.shares, row.price))
