def tensToString(num):
  tens = ['', '', 'twen', 'thir', 'four', 'fif', 'six', 'seven', 'eigh', 'nine']
  return tens[num]

def numberToString(num):
  ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen']
  if num < 0:
    print("invalid number")
    return None
  elif num >= 20:
    return tensToString(num//10) + 'ty' + numberToString(num%10)
  elif num > 15:
    return numberToString(num%10) + 'teen'
  else:
    return ones[num]

def magicNumber(number):
  # print(numberToString(number))
  print(number, "is", len(numberToString(number)))
  if len(numberToString(number)) == 4:
    print("4 is the magic number.")
    return
  
  return magicNumber(len(numberToString(number)))