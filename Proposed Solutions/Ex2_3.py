# import tracemalloc

# tracemalloc.start()
# from Ex2_1 import read_dict

# rows = read_dict("../Data/ctabus.csv")
# rt22 = [row for row in rows if row["route"] == "22"]
# print(max(rt22, key=lambda row: row["rides"]))
# print(tracemalloc.get_traced_memory())
# 179 Mb

# import tracemalloc

# tracemalloc.start()
# import csv

# f = open("../Data/ctabus.csv")
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = (dict(zip(headers, row)) for row in f_csv)
# rt22 = (row for row in rows if row["route"] == "22")
# print(max(rt22, key=lambda row: int(row["rides"])))
# print(tracemalloc.get_traced_memory())
# f.close()
# # 94 Mb "It's crazy"
