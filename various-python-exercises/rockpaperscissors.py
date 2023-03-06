import random
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

game_images_map = {0:rock, 1:paper, 2:scissors}

user = int(input("What do you choose? Type 0 => Rock, 1 => Paper or 2 => Scissors.\n  "))
pc = random.randint(0,2)

print(game_images_map[user])
print("Computer Chose: ")
print(game_images_map[pc])

if (user == 0 and pc == 0) or (user == 1 and pc == 1) or (user == 2 and pc == 2):
    print("Tie!")
elif (user == 0 and pc == 2) or (user == 1 and pc == 0) or (user == 2 and pc == 1):
    print("You win!")
elif (pc == 0 and user == 2) or (pc == 1 and pc == 0) or (pc == 2 and user == 1):
    print("You lose!")