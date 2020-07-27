import random

def guessNumber():
  upper_bound = int(input("Enter an upper bound "))
  count = 0
  answer = random.randint(1, upper_bound)
  # answer = random.randint(1, 100)
  print("Great! We have picked a number from 1 to", upper_bound, ". Now start guessing!")
  # guess = get_guess()
  guess = int(input("Guess a number "))
  count += 1

  while guess != answer:
    count += 1
    if guess > answer:
      print("Your guess is too big")
    else:
      print("Your guess is too small")
    # guess = get_guess()
    guess = int(input("Guess a number "))
  print("Yep! The number was", answer, ".")
  print("You got it in " + str(count) + " tries!")

quit = "y"
print("hello")
while quit == "y":
  user = input("What would you like to do today? ")
  words = user.split(" ")
  if words[0].lower() == "greet":
    for each in words[1:]:
      if each != "and":
        print("Hello,", each, "!")
  if words[0].lower() == "guess":
    guessNumber()
  quit = input("Anything else? y or n: ")