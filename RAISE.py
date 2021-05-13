#Raise raises the expection of any given value, so that it can be handled further up the stack

x = -1

if x < 0: # Raise an error and stop the program if x is lower than 0:
  raise Exception("Sorry, no numbers below zero")
