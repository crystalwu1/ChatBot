def convert(unitFrom, unitTo, num):
  if unitFrom == "ft" and unitTo == "in":
    print(num, unitFrom, "equals", float(num) * 12, unitTo)

  elif unitFrom == "in" and unitTo == "ft":
    print(num, unitFrom, "equals", float(num) / 12, unitTo)

  else:
    print("I don't recognize those units, sorry")