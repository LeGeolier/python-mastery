import stock


def print_table(obj, attr):
    for i in range(len(attr)):
        print(f"{attr[i] :>10}", end=" ")
    print()
    print(f"{"-"*10} " * len(attr))
    for record in obj:
        print(" ".join(f"{getattr(record,a):>10}" for a in attr))

portfolio = stock.read_portfolio('Data/portfolio.csv')
print_table(portfolio, ['name','shares','price'])
