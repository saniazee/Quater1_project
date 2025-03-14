import random

def play_rock_paper_scissors():

     print("Welcome to play rock,scissor,paer Game: ")
     print("----------------------------------------")

     rounds = 0
     computer_score = 0
     user_score = 0

     for i in range(5):
       rounds += 1
       options = ["rock","scissor","paper"]
       user_choice:str = input("Enter your choice (rock, paper, or scissors): ").lower()

       while user_choice not in options:
         print("invalid choice.Please enter correct choice! ")
         user_choice:str = input("Enter your choice (rock, paper, or scissors): ").lower()

       computer_choice = random.choice(options)
       print(f"You chose {user_choice}:")
       print(f"Computer chose {computer_choice}")

       if user_choice == computer_choice:
          print("Its a tie! ")
       elif(user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
          print("You win! ")
          user_score +=1
       else:
         print("Computer wins!")
         computer_score += 1

       

     print(f"Total Round is {rounds}.Computer score is {computer_score} and user score is {user_score}" )

play_rock_paper_scissors()