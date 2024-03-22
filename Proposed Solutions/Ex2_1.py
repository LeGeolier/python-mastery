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

import csv


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
