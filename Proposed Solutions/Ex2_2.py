# I'll adjust the code by using what info we were provided before
# as such i'll be using slotted class and not dict


import csv


class Row:
    __slots__ = ["name", "shares", "price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skipping header
        for row in rows:
            portfolio.append(Row(name=row[0], shares=int(row[1]), price=float(row[2])))
        return portfolio
