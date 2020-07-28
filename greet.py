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