import guessnumber
import greet
import unitconversion
import magic4

print("Hello!")
user = input("What would you like to do today? ")
name = None

while user != "user" or user != "no":

  try:

    words = user.split(" ")

    if words[0].lower() == "greet":
      name = greet.greet(words, name)

    elif words[0].lower() == "guess":
      guessnumber.guessNumber()

    elif words[0].lower() == "convert":
      unitconversion.convertMetric(words[2], words[4], words[1])

    elif words[0].lower() + words[1].lower() == "magicnumber":
      num = input("Choose an integer from 1 to 99: ")
      magic4.magicNumber(int(num))

    else:
      print("I don't recognize that command.")
    
    print("")
    user = input("Anything else? ")

  except:
    print("")
    user = input("Invalid input. Try again: ")

print("Goodbye!")