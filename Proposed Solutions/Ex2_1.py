# Part 1
""" 
import tracemalloc
f = open('../Data/ctabus.csv')
tracemalloc.start()
data = f.read()
f.close()
print(f"Length data : {len(data)}") # 12.361.039
current, peak = tracemalloc.get_traced_memory()
print(f"Current : {current}") # ~12Mb
print(f"Peak : {peak}") # ~38Mb
"""

# Part 2
""" 
import tracemalloc
f = open('../Data/ctabus.csv')
tracemalloc.start()
lines = f.readlines()
f.close()
print(f"Length lines : {len(lines)}") # 577.564
current, peak = tracemalloc.get_traced_memory()
print(f"Current : {current}") # ~40mb
print(f"Peak : {peak}") # ~40Mb 
"""

# Part (c) List of Tuples

# import csv


# def read_rides_as_tuples(filename):
#     """
#     Read the bus ride data as a list of tuples
#     """
#     records = []
#     with open(filename) as f:
#         rows = csv.reader(f)
#         _ = next(rows)
#         for row in rows:
#             route = row[0]
#             date = row[1]
#             daytype = row[2]
#             rides = int(row[3])
#             record = (route, date, daytype, rides)
#             records.append(record)
#     return records


# if __name__ == "__main__":
#     import tracemalloc

#     tracemalloc.start()
#     rows = read_rides_as_tuples("../Data/ctabus.csv")
#     print("Memory Use : Current %d, Peak %d" % tracemalloc.get_traced_memory())
#     # Resulted around 114Mb

# Part (d) Memory use of other data structures


# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


# A class with __slots__
class RowSlot:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


from collections import namedtuple

RowTuple = namedtuple("RowTuple", ["route", "date", "daytype", "rides"])


import csv


def read_namedtuples(filename):
    # Memory used : ~120Mb
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            tupledRow = RowTuple(row[0], row[1], row[2], int(row[3]))
            records.append(tupledRow)
    return records


def read_tuples(filename):
    # Memory used : ~115 Mb
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_dict(filename):
    # Memory used : ~180Mb
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = {
                "route": row[0],
                "date": row[1],
                "daytype": row[2],
                "rides": int(row[3]),
            }
            records.append(record)
    return records


def read_instance(filename):
    # Memory used : ~130Mb
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            instance = Row(row[0], row[1], row[2], int(row[3]))
            records.append(instance)
    return records


def read_slots(filename):
    # Memory used ~110Mb it looks like
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            instance = RowSlot(row[0], row[1], row[2], int(row[3]))
            records.append(instance)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_namedtuples("../Data/ctabus.csv")
    print("Memory Use : Current %d, Peak %d" % tracemalloc.get_traced_memory())
    # Resulted around 114Mb

""" 
Seems like the best option is using slots
"""
