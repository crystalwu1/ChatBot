
def convertMetric(unitFrom, unitTo, num):
  units = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

  indexFrom = units.index(unitFrom)
  indexTo = units.index(unitTo)
  diff = indexFrom - indexTo

  if diff > 0:
    #going to larger units
    print(num, unitFrom, "equals", float(num) * (10 ** diff), unitTo)
  else:
    #going to bigger units
    print(num, unitFrom, "equals", float(num) * (10 ** diff), unitTo)

def convert(unitFrom, unitTo, num):
  if unitFrom == "ft" and unitTo == "in":
    print(num, unitFrom, "equals", float(num) * 12, unitTo)

  elif unitFrom == "in" and unitTo == "ft":
    print(num, unitFrom, "equals", float(num) / 12, unitTo)

  elif unitFrom == "C" and unitTo == "F":
    print(num, unitFrom, "equals", float(num*9/5+32) / 12, unitTo)

  elif unitFrom == "F" and unitTo == "C":
    print(num, unitFrom, "equals", float((num - 32)*5/9) / 12, unitTo)

  else:
    print("I don't recognize those units, sorry")