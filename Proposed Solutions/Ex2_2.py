# I'll adjust the code by using what info we were provided before
# as such i'll be using slotted class and not dict


import csv

""" 
class Row:
    __slots__ = ["name", "shares", "price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"name : {self.name} shares : {self.shares} price : {self.price}"

    def __str__(self):
        return f"name : {self.name} shares : {self.shares} price : {self.price}"


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skipping header
        for row in rows:
            portfolio.append(Row(name=row[0], shares=int(row[1]), price=float(row[2])))
        return portfolio


portfolio = read_portfolio("../Data/portfolio.csv")
from pprint import pprint

pprint(portfolio) """

# Was a good thinking but actually it complicate the exercice ...


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio("../Data/portfolio.csv")
from pprint import pprint

from Ex2_1 import read_dict

# pprint(portfolio)

rows = read_dict("../Data/ctabus.csv")
# 1. How many bus routes exist in Chicago
routes = set()
for row in rows:
    routes.add(row["route"])

""" print(routes)
print(len(routes)) """

# 2. How many people rode the number 22 bus on february 2 2011 What about any route on any date of your choosing
# datechosen = input("Please select a date format mm/dd/YYYY\n")
# c = 0
# for row in rows:
#     if row["date"] == datechosen:
#         c += 1
# print(c)
# 3. What is the total number of rides taken on each bus route
from collections import Counter

myCount = Counter
for row in rows:
    if myCount[row["route"]]:
        myCount[row["route"]] += 1
    else:
        myCount[row["route"]] = 0
print(myCount)

# 4. What five bus routes had the greatest ten-year icrease in ridership from 2001 to 2011
