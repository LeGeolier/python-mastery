import reader
import stock
import tableformat

portfolio = reader.read_csv_as_instances("Data/portfolio.csv", stock.Stock)
formatter = tableformat.create_formatter("text")

with stock.redirect_stdout(open("out.txt", "w")) as file:
    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)
print(open("out.txt").read())
