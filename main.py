import guessnumber

def greet(words, name):
  for each in words[1:]:
    if each == "me":
      if name != None:
        print("Hello,", name, "!")
      else:
        name = input("I don't know your name. What is is? ")
        greet(words, name)
        return name
        
    elif each != "and":
      print("Hello,", each, "!")
  return name
  
  
def convert(unitFrom, unitTo, num):
  if unitFrom == "ft" and unitTo == "in":
    print(num, unitFrom, "equals", float(num) * 12, unitTo)

  elif unitFrom == "in" and unitTo == "ft":
    print(num, unitFrom, "equals", float(num) / 12, unitTo)

  else:
    print("I don't recognize those units, sorry")

print("Hello!")
quit = input("What would you like to do today? ")
name = None

while quit != "quit" or quit != "no":
  
  words = quit.split(" ")

  if words[0].lower() == "greet":
    name = greet(words, name)

  elif words[0].lower() == "guess":
    guessnumber.guessNumber()

  elif words[0].lower() == "convert":
    convert(words[2], words[4], words[1])

  else:
    print("I don't recognize that command.")
  
  print("")
  quit = input("Anything else? ")

print("Goodbye!")