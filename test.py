from reader import DictCSVParser

parser = DictCSVParser([str, int, float])
port = parser.parse("Data/portfolio.csv")
