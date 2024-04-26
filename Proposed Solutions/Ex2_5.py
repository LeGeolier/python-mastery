import collections.abc
import csv
import sys

# items = []
# print(sys.getsizeof(items))
# items.append(1)
# print(sys.getsizeof(items))
# items.append(2)
# print(sys.getsizeof(items))
# items.append(3)
# print(sys.getsizeof(items))
# items.append(4)
# print(sys.getsizeof(items))
# items.append(5)
# print(sys.getsizeof(items))

row = {"route": "22", "date": "01/01/2001", "daytype": "U", "rides": 7354}
# print(sys.getsizeof(row))  # 184
row["a"] = 1
# print(sys.getsizeof(row))  # 184
row["b"] = 2
# print(sys.getsizeof(row))  # 272
del row["b"]
# print(sys.getsizeof(row))  # 272


def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytype=daytypes, numrides=numrides)


import collections
import tracemalloc

# tracemalloc.start()
# columns = read_rides_as_columns("../Data/ctabus.csv")
# print(tracemalloc.get_traced_memory())


class RideData(collections.abc.Sequence):
    def __init__(self, d=None):
        if d == None:
            self.routes = []
            self.dates = []
            self.daytypes = []
            self.numrides = []
        else:
            self.routes = d["route"]
            self.dates = d["date"]
            self.daytypes = d["daytype"]
            self.numrides = d["rides"]

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        d = {
            "route": self.routes[index],
            "date": self.dates[index],
            "daytype": self.daytypes[index],
            "rides": self.numrides[index],
        }
        return RideData(d)

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])

    def __repr__(self):
        return repr(list(zip(self.routes, self.dates, self.daytypes, self.numrides)))


# Re writing read_rides_as_dicts
def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
    return records


rows = read_rides_as_dicts("../Data/ctabus.csv")
# print(repr(rows))
# print(len(rows))
r = rows[0:10]
print(len(r))
print(r[0])
