import random
def computer_guess(low,high):

   guess_count = 0

   while True:
    if low != high:
      guess = random.randint(low,high)
    else:
      guess= low

    user_input = input(f"Is {guess} the correct number? (yes/no): ").lower()
    guess_count +=1

    if user_input == "yes":
      print(f"Guessed the number in {guess_count} tries:")
      break
    elif user_input == "no":
     user_input_high_low = input(f"is your number is lower and higher than {guess}? ").lower()
     if user_input_high_low == "higher":
       low = guess + 1
     elif user_input_high_low == "lower":
       high = guess - 1
     else:
      print("invalid input.Please enter 'highe' or 'lower'.")

    else:
       print("Invalid input. Please enter 'yes' or 'no'.")




computer_guess(10,50)