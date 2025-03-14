import random

words = ["orange","apple","banana","grape","pineapple"]


hangman_art = {0: ("     ",
                   "     ",
                   "     " ),
               1:  ("  o  ",
                   "     ",
                   "     " ),
               2: ("  o  ",
                   "  |  ",
                   "     " ),
               3: ("  o  ",
                   " /|  ",
                   "     " ),
               4:  (" o  ",
                   " /|\\ ",
                   "     " ),
               5:  (" o  ",
                   " /|\\ ",
                   " /   " ),
               6:  ("  o ",
                    " /|\\ ",
                    " / \\"),}

def display_man(wrong_gusses):
    print("***************")

    for line in hangman_art[wrong_gusses]:
       print(line)

    print("***************")

def  display_hint(hint):

    print(" ".join(hint))

def   display_answer(answer):
   print(" ".join(answer))


def main():

   answer = random.choice(words)
   hint = ["-"] * len(answer)
   wrong_gusses = 0
   is_running = True

   while is_running:
    display_man(wrong_gusses)
    display_hint(hint)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("invalid input! ")
      continue

    if guess in answer:
     for i in range(len(answer)):
      if answer[i] == guess:
         hint[i] = guess
      else:
         pass   
    else:
       wrong_gusses +=1

    if "-" not in hint:
        display_man(wrong_gusses)
        display_answer(answer)
        print("you won! ")
        is_running = False
        break
    elif wrong_gusses >= len(hangman_art) - 1:
        display_man(wrong_gusses)
        display_answer(answer)
        print("you lose! ")
        is_running = False
        break




if __name__ == "__main__":
   main()