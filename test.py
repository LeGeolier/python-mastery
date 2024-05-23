from stock import SimpleStock

goog = SimpleStock("GOOG", 100, 490.10)
ibm = SimpleStock("IBM", 50, 91.23)

print(goog.__class__)

print(ibm.__class__)
print(goog.cost())
print(ibm.cost())
print(SimpleStock.__dict__["cost"](goog))
print(SimpleStock.__dict__["cost"](ibm))
