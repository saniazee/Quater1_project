import random
import string

def passward_creator():

  characters = string.ascii_letters + string.digits + string.punctuation
  passward_length:int  = int(input("how long you want the passward to be? "))
  passward = ""

  for i in range(0,passward_length):
     passward_selection = random.choice(characters)
     passward += passward_selection
  print(f"your selected passward is {passward}: ")


passward_creator()
