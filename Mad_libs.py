def madlib(noun,verb,adjective):




  print(f" It was a {adjective} summer day. I was walking my {noun} in the park when suddenly,\n I saw a {adjective} {noun} flying through the air.\n It landed right in front of me,\n and I couldn't believe my {noun}! I decided to {verb} it home and show my {noun}.")


def main():

   print("--------------------")
   print(" welcome to madlib: ")
   print()
   try:
     noun:str = input("Enter a Noun: ")
     verb:str = input("Enter a verb: ")
     adjective:str = input("Enter an adjective: ")
     madlib(noun,verb,adjective)
   except TypeError:
    print("Invalid input type. Please enter strings for noun, verb, and adjective.")
   except Exception as e:
    print(f"An error occured: {e}")


main()