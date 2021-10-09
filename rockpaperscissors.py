rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#####################################################
import random

#Rock WINS against scissors
#Scissors WINS against paper
#Paper WINS against rock

choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if player_choice == "0":
    print(f"You chose: {rock}")
    if computer_choice == choice_list[2]:
        print(f"Computer chose: {computer_choice}\n You Win!")
    elif computer_choice == choice_list[0]:
        print(f"Computer chose: {computer_choice}\n Draw!")
    else:
        print(f"Computer chose: {computer_choice}\n You Lose.")

if player_choice == "1":
    print(f"You chose: {paper}")
    if computer_choice == choice_list[0]:
        print(f"Computer chose: {computer_choice}\n You Win!")
    elif computer_choice == choice_list[1]:
        print(f"Computer chose: {computer_choice}\n Draw!")
    else:
        print(f"Computer chose: {computer_choice}\n You Lose.")


if player_choice == "2":
    print(f"You chose: {scissors}")
    if computer_choice == choice_list[1]:
        print(f"Computer chose: {computer_choice}\n You Win!")
    elif computer_choice == choice_list[2]:
        print(f"Computer chose: {computer_choice}\n Draw!")
    else:
        print(f"Computer chose: {computer_choice}\n You Lose.")


