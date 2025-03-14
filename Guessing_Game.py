import random

def guess_number(user_guess):

       computer_guess = random.randint(0,100)

       while user_guess != computer_guess:
            if user_guess< computer_guess:
               print("yours guess is too low: ")
            elif user_guess > computer_guess:
               print("your guess is too high: ")

            user_guess:int = int(input("Enter the number from 0 to 100: "))
       print(f"congrats! The number is {computer_guess}")


def main():

     print("-----------------------------------")
     print("Welcome the guess the number game: ")
     print("Guess the number between 0 to 100: ")
     print()


     user_guess:int = int(input("Enter the number from 0 to 100: "))
     guess_number(user_guess)









main()