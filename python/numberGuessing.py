from random import randint

def getLimit():
  try:
    val = int(input("Please input an upper limit for the computer to pick from: "))
    if(val < 1):
      raise ValueError
    return val
  except ValueError:
    print("Invalid input! Try again!")
    return getLimit()
  
def getUserGuess():
  try:
    guess = int(input("Please input a number: "))
    if(guess < 1):
      raise ValueError
    return guess
  except ValueError:
    print("Invalid input! Try again!")
    return getUserGuess()
  
def main():
  counter = 1
  limit = getLimit()
  value = randint(1, limit)
  user = getUserGuess()
  while(user != value):
    if(user > value):
      print("Your number is greater than the computer chosen value")
    else:
      print("Your number is less than the computer chosen value")
    counter += 1
    user = getUserGuess()
  print("Well done! You solved it in", counter, "times!")

main()
