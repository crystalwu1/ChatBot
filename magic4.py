def numberToString(num):
  if num < 0:
    print("invalid number")
    return None
  elif num == 1:
    return 'one'
  elif num == 2:
    return 'two'
  elif num == 3:
    return 'three'
  elif num == 4:
    return 'four'
  elif num == 5:
    return "five"
  elif num == 6:
    return "six"
  elif num == 7:
    return 'seven'
  elif num == 8:
    return "eight"
  elif num == 9:
    return 'nine'
  elif num == 10:
    return "ten"
  # elif num == 11:
  #   return "eleven"
  # elif num == 12:
  #   return "twelve"
  # elif num == 13:
  #   return "thirteen"
  # elif num == 15:
  #   return "fifteen"
  # elif num % 10 == 0:
  #   return numberToString(num//10) + "ty"
  # else:
  #   return numberToString(num//10) + "ty" + numberToString(num%10)

def magicNumber(number):
  print(number, "is", len(numberToString(number)))
  if len(numberToString(number)) == 4:
    print("4 is the magic number.")
    return
  
  return magicNumber(len(numberToString(number)))