"""
import csv

coltypes = [str, int, float]
f = open("../Data/portfolio.csv")
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
r = list(zip(coltypes, row))
print(r)
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
# Without dict comprehension
d = dict(zip(headers, record))
print(d)
# With dict comprehension
d2 = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(d2)
"""

import csv


def read_csv_as_dicts(filename, dict_struct):
    resp = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            d = {name: func(val) for name, func, val in zip(headers, dict_struct, row)}
            resp.append(d)
    return resp


rows = read_csv_as_dicts("../Data/ctabus.csv", [str, str, str, int])
print(len(rows))

routeids = {id(row["route"]) for row in rows}
print(len(routeids))

# I don't know why
a = "ADPHGRZSPIVHSPIjipjgfipfjsigjpojgqiphipghrqjb"
b = "ADPHGRZSPIVHSPIjipjgfipfjsigjpojgqiphipghrqjb"
print(a is b)

import sys

a = sys.intern(a)
b = sys.intern(b)
print(a is b)
