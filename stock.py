# stock.py
import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    resp = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            S = Stock(row[0], int(row[1]), float(row[2]))
            resp.append(S)
    return resp


def print_portfolio(portfolio):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print(("-" * 10 + " ") * 3)
    for row in portfolio:
        print("%10s %10d %10.2f" % (row.name, row.shares, row.price))


# portfolio = read_portfolio("Data/portfolio.csv")
# for s in portfolio:
#     print(repr(s))
# print_portfolio(portfolio=portfolio)
